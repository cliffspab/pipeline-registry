# Architecture and authority

## Authority chain

1. The supervisor controls scope, edition identity and publication.
2. `Blueprint/BLUEPRINT.md` is the single editable modular authority.
3. `Blueprint/build.py` validates and generates all text, routed, skill, ZIP
   and receipt surfaces.
4. `Blueprint/build_human_volume.py` generates the Word reading volume from
   the same source and embeds its edition and source hash.
5. Git commit identity plus successful GitHub validation confirms publication.
6. The exact validated commit is copied to the three cloud destinations.

Generated outputs and cloud mirrors are never independent authority.

## Components and invariants

The master contains exactly one each of Boot, Edit, Check, Photo, PR and Thai
Places. Unmarked content between components is invalid. Boot contains the sole
House Essentials copy and the semantic routing table. Edit contains the common
method and embedded Directory. Thai Places remains a conditional lookup.

The build enforces six components, 37 routes, 21 real Markdown heading targets,
16 reference routes, 76 Thai provinces, deterministic ZIPs and matching edition
witnesses.

## Publication boundary

The cloud publisher does not copy the mutable working tree. It extracts
`Blueprint/` from the full commit SHA that passed GitHub validation into a
temporary directory, copies that immutable tree with `rclone copy`, performs a
one-way content check and inventories duplicate or remote-only paths. Remote
extras are reported and never deleted.

The same committed archive carries the portability ZIP, manifest and audit
snapshot to the separate Bangkok Post OneDrive portability backup.

After validation, the local Shift pickup is refreshed from generated outputs:
eight loose documents, six installable skill folders and six ZIPs. It is not
authority and is not mirrored as a separate cloud tree.

A successful run writes `.publication/last.json`. Normal success output is
short; detailed command output is reserved for failures.
