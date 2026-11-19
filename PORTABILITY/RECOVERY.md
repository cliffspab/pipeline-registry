# Recovery

Git history is the primary recovery mechanism. Do not use destructive resets or
force-pushes to repair a disputed state.

If the live tree is damaged:

1. Preserve the damaged tree and record its commit identity.
2. Clone the repository into a new directory.
3. Run the cold-rebuild checks.
4. Compare the clone with `PORTABILITY/snapshot/` and the portability manifest.
5. Restore through a reviewed commit, not by copying generated hosted outputs
   back into the repository.

`MASTER.md` is data, not an operational model input. Recovery must preserve its
exclusion from the published site.
