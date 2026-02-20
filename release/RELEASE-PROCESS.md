# Release Process (Final)

This is the final, working flow using the scripts in `ModbusMonitorXPF/DoRelease`.

## Windows PowerShell (recommended)

### 0) Build and publish EXEs

```powershell
cd C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\DoRelease
.\DoRelease.ps1
```

### 1) Publish EXEs to GitHub Release (from XPF output)

```powershell
cd C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\DoRelease
pwsh
.\Publish-GitHubRelease.ps1 -GenerateSha256 -UploadSha256 -Verbose
```

Optional (explicit tag):

```powershell
cd C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\DoRelease
pwsh .\Publish-GitHubRelease.ps1 -Tag v5.0.1.0 -GenerateSha256 -UploadSha256 -Verbose
```

### 2) Update docs download buttons + release docs, then publish MkDocs

```powershell
cd C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\DoRelease
pwsh .\Update-DocsDownloadLinks.ps1 -Commit -Push -Verbose
```

### 3) Optional validation-only docs run (no commit/push)

```powershell
cd C:\Users\prati\source\repos\Modbus-Monitor\ModbusMonitorXPF\DoRelease
pwsh .\Update-DocsDownloadLinks.ps1 -Verbose
```

## WSL equivalent

```bash
cd /mnt/c/Users/prati/source/repos/Modbus-Monitor/ModbusMonitorXPF/DoRelease
bash ./Publish-GitHubRelease.sh --generate-sha256 --upload-sha256 --verbose
bash ./Update-DocsDownloadLinks.sh --commit --push --verbose
```

## Important notes

- `Publish-GitHubRelease.ps1` reads release files from `C:\Publish\XPF` by default.
- Release assets remain versioned (for example: `Modbus-Monitor-XPF-5.0.1.0-x64-setup.exe`).
- `Update-DocsDownloadLinks.ps1 -Commit -Push` commits in `modbus-monitor-docs` and pushing triggers MkDocs deploy.

## If push is rejected (non-fast-forward)

If docs push fails because remote `main` is ahead and you have local unstaged changes:

```powershell
$repo = "C:\Users\prati\source\repos\Modbus-Monitor\modbus-monitor-docs"
git -C $repo stash push -m "temp-stash-before-rebase-docs-push"
git -C $repo pull --rebase origin main
git -C $repo push origin main
git -C $repo stash pop
```