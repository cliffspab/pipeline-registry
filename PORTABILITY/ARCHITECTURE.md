# Architecture and authority

## Purpose

The mechanism turns one approved modular Blueprint into reproducible skill,
lookup, reading and cloud-delivery surfaces. It keeps editorial authority,
build machinery and transport separate.

## Authority chain

1. The human supervisor authorises scope, edition identity and publication.
2. `Blueprint/BLUEPRINT.md` is the modular beta source for the six-skill set.
3. `Blueprint/build.py` validates and generates the deployment.
4. Generated files are evidence and delivery surfaces, never independent
   editorial authority.
5. Git commit identity plus successful GitHub validation confirms publication.
6. `Shift/` and the three cloud trees are generated pickup or mirror surfaces.

Repository administration must not become an editorial rule. Editorial content
must not be silently changed to accommodate transport machinery.

## Source and generated layout

`Blueprint/BLUEPRINT.md` contains six marked components:

- Boot: front-end router, House Essentials and hard invariants.
- Edit: common desk method and embedded Directory reference source.
- Check, Photo and PR: bounded task modules.
- Thai Places: conditional Thai-geography lookup.

`Blueprint/build.py` produces:

- complete `BLUEPRINT.txt` and Directory compatibility files;
- six routed Markdown files;
- six installable `SKILL.md` folders;
- six deterministic ZIP packages;
- indexes, hashes and a build receipt.

`Blueprint/build_human_volume.py` produces the Word reading volume. Root
`shift.py` creates the exact local pickup. Root `distribute_blueprint.py` waits
for GitHub validation and copies the complete registry `Blueprint/` tree to the
three approved cloud destinations.

## Distribution sequence

```text
approved source
    -> local build and byte comparison
    -> supervisor-reviewed push preflight
    -> Git commit and origin/main equality
    -> GitHub Linux validation
    -> exact local Shift refresh
    -> copy-only pCloud, Google Drive and OneDrive mirrors
    -> one-way source-to-remote verification
```

No cloud mirror is a source. `rclone copy`, not `rclone sync`, is intentional:
distribution may add or update source paths but does not delete remote extras.

## Hard invariants

- Edition identity matches across the complete generated set.
- The source contains exactly six recognised components.
- House Essentials occurs exactly once, in Boot.
- The semantic index has 37 routes: 21 heading routes and 16 reference routes.
- Thai Places contains the held 76-province register.
- Every generated skill passes the skill validator.
- Rebuilding produces byte-identical files on Windows and Linux.
- Publication requires local `HEAD == origin/main` and successful GitHub CI.
- Shift is regenerated only from the validated registry.
- Cloud copies exclude `__pycache__` and `*.pyc`, never contain credentials,
  and must pass one-way `rclone check`.

