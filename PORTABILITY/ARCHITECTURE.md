# Architecture

`Blueprint/MASTER.md` is the sole editable desk-content authority. It contains
the edition, output/deployment metadata and tagged content blocks.

`Blueprint/assemble.js` is the sole assembler. The desk page, userscript and
GitHub Pages workflow consume it. Operational Markdown and the standalone
Directory copies are built at the point of use rather than committed beside
the master.

GitHub Actions publishes the repository, excluding `MASTER.md`, plus assembled
files under `live/`. `live/DIRECTORY.txt` and `live/DIRECTORY.yaml` come from
`directoryText()` and therefore cannot drift from the Directory block.

Installable individual-skill ZIPs and the complete skill ZIP set are created
in memory by the desk tools from the current master when requested. Generated
ZIPs are not committed or maintained as another copy of the skills.

Word production is outside this architecture, portability kit and publication
process.

GitHub commit history is the archive for `Blueprint/MASTER.md` and all other
content. The portability kit contains process tools only; it neither snapshots
content nor changes for a content-only commit.
The Git commit SHA is the content version identifier. The edition field in the
master is descriptive metadata rather than an independent version system.

The former guarded batch publisher, cloud distribution, Shift refresher and
static Directory copies are retired. GitHub is the registry and publication
base.
