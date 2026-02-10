# Release Process

## For v5.1.0.0 and beyond:

1. Build 6 EXEs (x86/x64/arm64 setup + portable)
2. Place in `release/` folder
3. `git add . && git push` 
4. Go to GitHub → Create Release
   - Tag: `v5.1.0.0`
   - Title: `Modbus Monitor XPF v5.1.0.0`
   - Upload 6 EXEs + SHA256SUMS.txt
   - Publish
5. Delete EXEs from `release/` folder
6. `git add . && git commit -m "Clean up release folder after v5.1.0.0"`
7. `git push`
8. Update docs/releases/v5.1.0.0.md with changelog
9. Update docs/releases/index.md to mark as latest
10. `git push` (MkDocs auto-deploys)



## Options

# Option 1: Keep it manual (simpler)

You manually create releases on GitHub (like you just did for v5.0.0.0)
MkDocs workflow handles docs auto-build only
Just follow: Build EXEs → push to release/ folder → create GitHub release manually → delete local files → push cleanup

# Option 2: Fully automated (one tag push = everything)

Create a separate GitHub Actions workflow that listens for tag pushes (v*.*.*)
On tag: automatically creates GitHub release + uploads EXEs from release folder
No manual GitHub web UI clicks needed