# Dependencies, accounts and secrets

## Runtime

- Python 3.12 or newer.
- `PyYAML==6.0.3`.
- `python-docx==1.2.0`.
- Git.
- GitHub CLI authenticated to `cliffspab/pipeline-registry`.
- rclone.

GitHub Actions uses Python 3.12 and the same pinned PyYAML version. The Word
builder is local because its visual output is separately reviewed when changed.

## Cloud access

Required rclone remotes:

- `pCloud:`
- `GDrive:`
- `onedrivebkp:`

Approved destinations are the `pipeline-registry/Blueprint` tree on each
remote, with pCloud under `Public Folder`.

Never commit rclone configuration, OAuth tokens, GitHub tokens, browser
sessions or recovery codes. Restore them through `gh auth login` and
`rclone config`, then run:

```powershell
gh auth status
rclone listremotes
python bootstrap/distribute_blueprint.py --preflight
```

