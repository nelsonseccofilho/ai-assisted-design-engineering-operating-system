#Requires -Version 7.4
<#
.SYNOPSIS
  Controlled local QA for an exact, detached framework commit.
.DESCRIPTION
  Runs the same nine Python commands declared by static-qa.yml, rejects skipped
  tests, checks symlink capability and verifies an unmodified worktree.
  Local PASS is never evidence of GitHub-hosted CI execution.
.EXAMPLE
  pwsh -NoProfile -File .\scripts\qa_local.ps1 -ExpectedSha <full-40-character-commit-sha>
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-fA-F0-9]{40}$')]
    [string]$ExpectedSha,

    [string]$PythonExecutable = 'python'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$previousNativePref = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false
$previousBytecode = $env:PYTHONDONTWRITEBYTECODE
$env:PYTHONDONTWRITEBYTECODE = '1'
$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$logPath = Join-Path ([System.IO.Path]::GetTempPath()) (
    'framework-local-qa-' + $ExpectedSha.Substring(0, 12) + '-' +
    [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ') + '-' +
    [Guid]::NewGuid().ToString('N').Substring(0, 8) + '.log'
)
$logReady = $false
$originalLocation = Get-Location

function Write-QALog([string]$Message) {
    Write-Host $Message
    Add-Content -LiteralPath $script:logPath -Value $Message -Encoding utf8
}

function Invoke-NativeChecked([string]$Program, [string[]]$Arguments) {
    $output = @(& $Program @Arguments 2>&1 | ForEach-Object { [string]$_ })
    $exitCode = $LASTEXITCODE
    foreach ($line in $output) { Write-QALog $line }
    if ($exitCode -ne 0) {
        throw ('COMMAND_FAILED exit=' + $exitCode + ' command=' + $Program + ' ' +
            ($Arguments -join ' '))
    }
    return ($output -join "`n")
}

function Assert-Clean([string]$Phase) {
    $result = @(& git -C $script:root status --porcelain=v1 --untracked-files=all 2>&1)
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0 -or $result.Count -ne 0) {
        throw ('CHECKOUT_NOT_CLEAN_' + $Phase + ' ' + ($result -join '; '))
    }
    Write-QALog ('CHECKOUT_' + $Phase + '=CLEAN')
}

try {
    New-Item -ItemType File -Path $logPath -ErrorAction Stop | Out-Null
    $logReady = $true
    Write-QALog 'FRAMEWORK_LOCAL_QA=START'
    Write-QALog ('EXPECTED_SHA=' + $ExpectedSha.ToLowerInvariant())
    Write-QALog 'HOSTED_CI=NOT_VERIFIED'
    Write-QALog ('LOG=' + $logPath)

    $head = @(& git -C $root rev-parse HEAD 2>&1)
    if ($LASTEXITCODE -ne 0 -or $head.Count -ne 1 -or
        $head[0].Trim() -cne $ExpectedSha.ToLowerInvariant()) {
        throw 'SHA_MISMATCH'
    }

    $branch = @(& git -C $root symbolic-ref --quiet --short HEAD 2>$null)
    if ($LASTEXITCODE -eq 0 -and $branch.Count -ne 0) {
        throw 'CHECKOUT_MUST_BE_DETACHED'
    }
    Assert-Clean 'BEFORE'
    Set-Location -LiteralPath $root

    $workflow = Join-Path $root '.github/workflows/static-qa.yml'
    $expectedCommands = @(
        'python scripts/validate_framework.py'
        'python scripts/test_runtime_sync.py'
        'python scripts/test_methodology.py'
        'python scripts/audit_methodology.py --framework .'
        'python scripts/test_audit_methodology.py'
        'python scripts/test_onboarding.py'
        'python scripts/test_current_state.py'
        'python scripts/test_runtime_context.py'
        'python scripts/test_action_claim.py'
    )
    $declared = @(
        foreach ($line in (Get-Content -LiteralPath $workflow)) {
            if ($line -match '^\s*-\s+run:\s*(python\s+.+?)\s*$') {
                $Matches[1].Trim()
            }
        }
    )
    if ($declared.Count -ne $expectedCommands.Count) { throw 'WORKFLOW_COMMAND_COUNT_DRIFT' }
    for ($i = 0; $i -lt $expectedCommands.Count; $i++) {
        if ($declared[$i] -cne $expectedCommands[$i]) {
            throw ('WORKFLOW_COMMAND_DRIFT step=' + ($i + 1))
        }
    }
    Write-QALog 'WORKFLOW_PARITY=9/9_MATCH'

    $version = Invoke-NativeChecked $PythonExecutable @(
        '-c', 'import sys; print("PYTHON_VERSION=" + sys.version.split()[0]); sys.exit(0 if sys.version_info >= (3,12) else 2)'
    )
    if ($version -notmatch 'PYTHON_VERSION=') { throw 'PYTHON_VERSION_UNVERIFIED' }

    $probe = @'
import tempfile
from pathlib import Path
with tempfile.TemporaryDirectory(prefix="framework-symlink-qa-") as directory:
    root = Path(directory)
    target = root / "target.txt"
    link = root / "link.txt"
    target.write_text("fictional QA\n", encoding="utf-8")
    try:
        link.symlink_to(target)
    except OSError as error:
        print("SYMLINK_CAPABILITY=BLOCKED")
        print("WINERROR=" + str(getattr(error, "winerror", None)))
        raise SystemExit(2)
    if not link.is_symlink() or link.resolve() != target.resolve():
        print("SYMLINK_CAPABILITY=INVALID")
        raise SystemExit(3)
    print("SYMLINK_CAPABILITY=READY")
'@
    $probeResult = Invoke-NativeChecked $PythonExecutable @('-B', '-c', $probe)
    if ($probeResult -notmatch 'SYMLINK_CAPABILITY=READY') {
        throw 'SYMLINK_CAPABILITY_NOT_READY'
    }

    for ($i = 0; $i -lt $expectedCommands.Count; $i++) {
        $command = $expectedCommands[$i]
        $arguments = @('-B') + @($command.Substring(7) -split '\s+')
        Write-QALog ('=== STEP ' + ($i + 1) + '/9: ' + $command + ' ===')
        $result = Invoke-NativeChecked $PythonExecutable $arguments
        if ([string]::IsNullOrWhiteSpace($result)) {
            throw ('EMPTY_STEP_OUTPUT step=' + ($i + 1))
        }
        if ($result -match '(?i)\bskipped\b|\bskip=\d+\b|\bskips=\d+\b') {
            throw ('SKIPPED_TESTS_DETECTED step=' + ($i + 1))
        }
        if ($i -eq 6) {
            if ($result -notmatch 'Ran\s+8\s+tests' -or
                $result -notmatch '(?m)^OK\s*$' -or
                $result -notmatch 'test_base_contract_and_containment_of_resolved_links.*\.\.\. ok') {
                throw 'CURRENT_STATE_8_OF_8_NOT_CONFIRMED'
            }
        }
        Write-QALog ('STEP_' + ($i + 1) + '=PASS')
    }

    Assert-Clean 'AFTER'
    Write-QALog 'LOCAL_WORKFLOW_COMMANDS=9/9_PASS'
    Write-QALog 'CURRENT_STATE_TESTS=8/8_PASS'
    Write-QALog 'SKIPPED_TESTS=0'
    Write-QALog 'LOCAL_QA_RESULT=PASS'
    Write-QALog 'HOSTED_CI=NOT_VERIFIED'
}
catch {
    if ($logReady) {
        Write-QALog ('LOCAL_QA_RESULT=FAIL')
        Write-QALog ('FAILURE=' + $_.Exception.Message)
    }
    else {
        Write-Error $_.Exception.Message
    }
    throw
}
finally {
    Set-Location $originalLocation
    if ($null -eq $previousBytecode) {
        Remove-Item Env:PYTHONDONTWRITEBYTECODE -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONDONTWRITEBYTECODE = $previousBytecode
    }
    $PSNativeCommandUseErrorActionPreference = $previousNativePref
    Write-Host ('QA_LOG=' + $logPath)
}
