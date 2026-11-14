# Dependencies, accounts and secrets

## Required software

- Git, including access to `https://github.com/cliffspab/pipeline-registry`.
- Python 3 with PyYAML and python-docx for the complete build and Word volume.
- GitHub CLI (`gh`) authenticated to the registry account.
- rclone. On Windows the official installation command is:

  `winget install --id Rclone.Rclone --exact`

- Microsoft Word or the bundled document renderer is useful for visual Word
  inspection, but not required for the text build.

## Required services

- GitHub repository: `cliffspab/pipeline-registry`.
- GitHub Actions workflow: `Validate Blueprint beta`.
- rclone remotes with these exact configured names:
  - `pCloud:`
  - `GDrive:`
  - `onedrivebkp:`

Approved destinations:

- `pCloud:Public Folder/pipeline-registry/Blueprint`
- `GDrive:pipeline-registry/Blueprint`
- `onedrivebkp:pipeline-registry/Blueprint`

## Secrets policy

Never put rclone configuration, OAuth refresh tokens, GitHub tokens, browser
cookies or account-recovery material in Git, Shift, the Blueprint tree or this
kit. Reauthorise each service on the recovery machine:

1. Run `gh auth login` and confirm repository access with `gh auth status`.
2. Run `rclone config` and create or restore the three remote names.
3. Test read-only access with `rclone lsd REMOTE: --max-depth 1`.
4. Run `python distribute_blueprint.py --preflight` before any publication.

The rclone configuration normally lives outside the project. On Windows its
usual location is `%APPDATA%\rclone\rclone.conf`; treat that file as a secret.
Back it up only in an encrypted credential store.

