# BKPDE workspace

This workspace maintains the Bangkok Post desk master and its at-use assembler.

## Cold start

Read `00_START-HERE.md`, the supervisor's current instruction, the live files
and `COMMITS-PENDING.md`. Inspect the working tree and local/origin commit
identity before changing anything. Current files outrank old conversations.

## Authority and scope

The human is the supervisor. Ask before changing edition identity, publishing
or widening the agreed change. Use an isolated candidate for substantive
machinery work.

`Blueprint/MASTER.md` is the only editable desk-content authority. It contains
metadata and tagged content blocks. `Blueprint/assemble.js` produces the
Blueprint, skills, deployments and Directory copies at the point of use.
Generated outputs are not committed as parallel authorities.

Word production is outside this mechanism. Do not build, validate, publish or
include Word material in routine maintenance, recovery or release checks.

## Validation

Exercise every declared output, deployment and custom part through
`assemble.js`; validate `directoryText()`, JavaScript syntax and `git diff
--check`. Run `python PORTABILITY/verify_portability.py --live` after rebuilding
the portability kit.

## Publication

The retired `push.bat`, cloud distributor and Shift refresher are not part of
the architecture. After supervisor approval, commit the exact reviewed tree and
push it without rebasing. If upstream has advanced, stop, combine the state in
an isolated candidate and validate again.

GitHub Actions publishes the repository and the assembled `live/` outputs.
GitHub Pages must use **GitHub Actions** as its source. Publication is complete
only when local HEAD equals `origin/main`, the Pages workflow succeeds, the
hosted outputs show the committed edition and `Blueprint/MASTER.md` is absent
from the site.

## Directory, recovery and history

`live/DIRECTORY.txt` and `live/DIRECTORY.yaml` are deployment-time copies made
from the Directory block in `MASTER.md`. Do not restore static root copies.

`PORTABILITY/` is the self-contained recovery and audit kit. Rebuild it with
`python PORTABILITY/make_bundle.py`; verify it with `python
PORTABILITY/verify_portability.py --live`.

Record material changes in `CHANGELOG.md`, `VERSION_HISTORY.md` and
`COMMITS-PENDING.md`. Archive cleared pending entries when their exact commit is
published.
