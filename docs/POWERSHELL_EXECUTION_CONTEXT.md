# PowerShell execution context — explicit directory, repository and source identity

**Status:** proposed reusable execution rule, for review after published v3.9.0.  
**Owner:** public framework (FRAMEWORK_OWNED).  
**Scope:** PowerShell snippets handed to an operator for diagnostics, Git/API commands, build, tests, QA, checkout and release operations.

## Decision

A snippet must **never rely on the operator's current PowerShell prompt**. Even a snippet whose file paths are absolute or otherwise independent of the current directory should explicitly establish its intended working context, make that context observable and restore the prior location. Having a working command is not sufficient evidence that it was executed against the intended repository or source snapshot.

This is a source-execution discipline, **not** a new access permission, test pass, project adoption or ability to operate the user's computer.

## Required behavior

1. Set an explicit directory (`$dir`) and capture the entry directory (`$original = (Get-Location).Path`). Validate the expected working directory with `Test-Path -LiteralPath ... -PathType Container` **before** changing to it.
2. Use `Set-Location -LiteralPath $dir` before the operation. Print `DIRETORIO_ATUAL`. Use `try { ... } finally { Set-Location -LiteralPath $original }` for every such runnable snippet, and print the restored directory.
3. For a repository operation, independently validate Git root (`git rev-parse --show-toplevel`), remote origin (`git remote get-url origin`) and immutable full expected SHA (`git rev-parse HEAD`) **before** any QA, source claim or mutation. Check `$LASTEXITCODE` after every native command. Do not proceed on missing or mismatched values.
4. For isolated exact-SHA QA, additionally require detached HEAD via `git rev-parse --abbrev-ref HEAD` returning `HEAD` and `git status --porcelain=v1 --untracked-files=all` empty before and after QA. Never call `.Trim()` on a potentially null result such as `git branch --show-current` in a detached checkout.
5. For inspecting a **previous** failure, use the checkout and immutable SHA **that produced the original report**, not a subsequently repaired branch head. Read the existing report by an absolute path. Do not rerun or overwrite prior diagnostics without a separate request. A prior `FAIL` remains `FAIL`.
6. If the task does not involve a Git repository, select its actual workspace directory and verify the relevant absolute file paths; do **not** invent or assert a Git SHA. Keep incidental files/logs outside version control and do not print or upload private tokens, user directories or source data into a public audit receipt.
7. On an error or a partial write, stop and report the verified state. Never silently switch repository, directory or SHA, downgrade QA requirements, erase files, force reset, or retry an irreversible publication without readback and separate authority.

## Template: operator-run exact-SHA checkout QA

Fill in the repository URL, **existing checkout directory**, SHA and actual QA command. This template deliberately does **not** clone, reset or clean anything.

```powershell
& {
    $ErrorActionPreference = 'Stop'
    $PSNativeCommandUseErrorActionPreference = $false

    $original = (Get-Location).Path
    $repo = 'https://github.com/OWNER/REPOSITORY.git'
    $sha = '<exact-full-40-character-sha>'
    $dir = Join-Path $env:TEMP 'existing-isolated-checkout'

    try {
        if (-not (Test-Path -LiteralPath $dir -PathType Container)) {
            throw "Checkout not found: $dir"
        }

        Set-Location -LiteralPath $dir
        Write-Host "DIRETORIO_ATUAL=$((Get-Location).Path)"

        $root = git rev-parse --show-toplevel
        if ($LASTEXITCODE -ne 0 -or
            [IO.Path]::GetFullPath($root) -ine
            [IO.Path]::GetFullPath($dir)) {
            throw 'Unexpected Git root.'
        }

        $origin = git remote get-url origin
        if ($LASTEXITCODE -ne 0 -or $origin -ne $repo) {
            throw 'Unexpected Git remote.'
        }

        $actual = git rev-parse HEAD
        if ($LASTEXITCODE -ne 0 -or $actual -ne $sha) {
            throw 'Unexpected HEAD.'
        }

        $branch = git rev-parse --abbrev-ref HEAD
        if ($LASTEXITCODE -ne 0 -or $branch -ne 'HEAD') {
            throw 'Detached HEAD required.'
        }

        $before = @(git status --porcelain=v1 --untracked-files=all)
        if ($LASTEXITCODE -ne 0 -or $before.Count -ne 0) {
            throw 'Worktree is not clean.'
        }

        # Use the exact review-approved QA command here, check its exit code.
        & pwsh -NoProfile -File '.\scripts\qa_local.ps1' -ExpectedSha $sha
        if ($LASTEXITCODE -ne 0) {
            throw 'Local QA failed; do not claim PASS.'
        }

        $afterSha = git rev-parse HEAD
        if ($LASTEXITCODE -ne 0 -or $afterSha -ne $sha) {
            throw 'Checkout HEAD changed.'
        }

        $after = @(git status --porcelain=v1 --untracked-files=all)
        if ($LASTEXITCODE -ne 0 -or $after.Count -ne 0) {
            throw 'Checkout changed during QA.'
        }

        Write-Host "QA_SOURCE_SHA=$sha"
        Write-Host 'CHECKOUT_AFTER=CLEAN'
    }
    finally {
        Set-Location -LiteralPath $original
        Write-Host "DIRETORIO_RESTAURADO=$((Get-Location).Path)"
    }
}
```

## Template: prior diagnostic, READ_ONLY

Use the same root, origin and SHA checks above but point `$dir` to **the original failed checkout** and read `$reportFile = Join-Path $env:TEMP '<existing-report-name>.json'` after testing that file exists; print top-level `assessment` and `errors` **and** any nested diagnostics. No QA command is executed. A returned nested `errors=[]` does not override top-level failure or a nonzero original exit code.

## Governance and release boundary

Apply this rule to newly authored operator blocks after review. Its addition to public `main` does **not** rewrite the immutable v3.9.0 tag, retroactively make any historical run compliant or automatically update private adopters. Review the documentation PR, run relevant exact-SHA QA and publish/adopt by the normal separate version gates. Project-specific examples, private source logs and operator identity remain in their owning private runtime.
