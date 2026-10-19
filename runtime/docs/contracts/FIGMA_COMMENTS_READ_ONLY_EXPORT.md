# Figma comments: read-only export, validation and triage

**Ownership:** SHARED PROCEDURE · generic/framework-only.  
**Status:** OPERATIONALLY VALIDATED IN AN ADOPTING RUNTIME · no generic app installation requirement.  
**Scope:** Figma Design files, PowerShell 7, read-only Figma API, private evidence handling.  
**Related:** [Comment triage seed](../templates/COMMENT_TRIAGE.md), [Evidence reconciliation](EVIDENCE_RECONCILIATION.md), [Validation and closure](VALIDATION_AND_CLOSURE.md).

## Principle

Export comment evidence once, preserve the dated raw snapshot, compare root discussion IDs across snapshots, then scope discussions to the correct Figma page through current node ancestry. **Do not treat the exported file as a live state, resolve discussion roots automatically, or count replies as new discussions.**

This procedure was recovered from a previously successful SecretStore-based workflow and validated again in PowerShell 7.4 with an existing vault. The validation used a private adopting project; **do not copy private file keys, operator names, tokens, file URLs or comment exports into this public framework**.

## Prerequisites (one-time)

- A Personal Access Token with Figma comments read capability, created/stored by the operator; never print, commit or send it to chat.
- PowerShell 7 with Microsoft.PowerShell.SecretManagement and Microsoft.PowerShell.SecretStore available (or an equivalent secrets provider compatible with Get-Secret).
- A locally registered/accessible vault and an operator-known secret name. The example uses generic placeholder values; replace before execution.
- The target Figma **file key**, not a page node ID. The REST comments endpoint is **file-wide**.

The secured vault may prompt for its own password. The password is not the Figma API token.

### Recovery when Get-Secret is not recognized

Diagnose module discovery **before reinstalling or recreating the vault**:

~~~powershell
Get-Module -ListAvailable | Where-Object Name -Match 'SecretManagement|SecretStore' | Select-Object Name,Version,Path
$env:PSModulePath -split ';'
~~~

If modules were intentionally installed in an alternate user-owned directory, prepend their actual parent directory to the module search path **for this session only**:

~~~powershell
$moduleRoot = 'PATH-TO-EXISTING-MODULE-DIRECTORY'
if (-not (Test-Path $moduleRoot)) { throw 'Existing module directory missing.' }
$env:PSModulePath = "$moduleRoot;$env:PSModulePath"
Import-Module Microsoft.PowerShell.SecretManagement -ErrorAction Stop
Import-Module Microsoft.PowerShell.SecretStore -ErrorAction Stop
Get-SecretVault
~~~

A previously registered vault and encrypted data can exist even if module files are absent. Do **not** unregister/reset the old vault, call Reset-SecretStore, create a new token or use administrator installation merely because modules are undiscoverable. The previous adopting-runtime recovery downloaded Microsoft.PowerShell.SecretManagement 1.1.2 and Microsoft.PowerShell.SecretStore 1.0.6 from the official PowerShell Gallery to a user-local modules directory after other installation methods failed; this is a recovery example, **not** a default instruction to reinstall.

## Run: export the original Figma comments response

Update only the first four variables. Run in PowerShell 7 after vault/module access is confirmed:

~~~powershell
$ErrorActionPreference = 'Stop'
$fileKey = 'REPLACE-WITH-FIGMA-FILE-KEY'
$vaultName = 'REPLACE-WITH-EXISTING-VAULT-NAME'
$secretName = 'REPLACE-WITH-EXISTING-SECRET-NAME'
$outputDirectory = Join-Path (Get-Location).Path 'comentarios'

& {
    $token = Get-Secret -Name $secretName -Vault $vaultName -AsPlainText -ErrorAction Stop
    try {
        if ([string]::IsNullOrWhiteSpace($token)) {
            throw 'Figma token not recovered.'
        }
        $url = "https://api.figma.com/v1/files/$fileKey/comments?as_md=true"
        $result = Invoke-RestMethod -Uri $url -Headers @{'X-Figma-Token'=$token} -ErrorAction Stop

        if ($null -eq $result -or $null -eq $result.comments) {
            throw 'Invalid API response: comments array missing. Export not written.'
        }

        New-Item -ItemType Directory -Path $outputDirectory -Force -ErrorAction Stop | Out-Null
        $timestamp = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'
        $destination = Join-Path $outputDirectory "figma-comments-$timestamp.json"

        $result | ConvertTo-Json -Depth 100 |
            Set-Content -LiteralPath $destination -Encoding utf8 -ErrorAction Stop

        $comments = @($result.comments)
        $roots = @($comments | Where-Object { -not $_.parent_id })
        $resolved = @($roots | Where-Object { $_.resolved_at })
        Write-Host "Exported to: $destination"
        Write-Host "Entries: $($comments.Count)"
        Write-Host "Discussion roots: $($roots.Count)"
        Write-Host "Resolved: $($resolved.Count)"
        Write-Host "Open: $($roots.Count - $resolved.Count)"
    }
    finally {
        Remove-Variable token -ErrorAction SilentlyContinue
    }
}
~~~

No hard-coded minimum count: a small/new file can legitimately have few comments. If the current API response is inconsistent with a prior large snapshot, **stop and investigate** rather than silently accepting a zero/null file or overwriting existing evidence.

The script uses a date-stamped filename and does not overwrite prior snapshots. The full export may contain sensitive company and user information and must be stored with appropriate project-specific access controls; only metadata and derived non-sensitive method belong in the public framework.

## Interpretation: root threads and page scoping

- **Root discussion:** comment with empty/null parent_id. Replies have parent_id set and must be linked to the parent rather than counted as additional discussions.
- **Resolved:** root has non-null resolved_at. A 'done' message in a reply is **not** evidence of Figma-native resolution.
- **Open:** root resolved_at null; this is **not** automatically an unimplemented product task.
- **Comparison over time:** use stable root id to identify newly created roots, transitions open→resolved, reopened resolved→open and any roots no longer returned. Show resolved/new roots separately so additions do not conceal progress.
- **Page restriction:** Figma REST comments is file-scoped, not page-scoped. For a page-only audit, reconcile each root's client_meta.node_id / stable_path against **current** Figma node ancestry to the target page. A page-root anchor can refer to content anywhere on that page. Node IDs that no longer exist are orphans requiring historical context and should be marked UNKNOWN rather than assigned by prefix alone.
- **Source authority:** current Figma page geometry and manually updated design override stale analysis, but comments, design implementation, stakeholder acceptance and technical QA are distinct evidence categories.

## Closure and repeatability

Use [COMMENT_TRIAGE](../templates/COMMENT_TRIAGE.md) and record source filename, export time, file key in private context, page filter method, unique discussion root IDs and explicit unresolved questions. Preserve exact original timestamp, ID, author and message in private evidence; do not publish them. Maintain previous snapshots for ID-level comparison.

When a change is verified in design, it does not automatically resolve its Figma comment. Figma-native resolution, current implementation, and Product sign-off must be tracked separately. Read-only analysis does not grant permission to mutate the Figma file, comments, consumers, or the Design System.

**Recovery lesson:** once a secure token/vault flow has been validated, check module discovery/configuration first; avoid repeated package-install experiments, resetting vaults, generating tokens, or broad tests unless a new distinct failure warrants them.
