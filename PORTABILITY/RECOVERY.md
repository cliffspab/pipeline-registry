# Recovery

Git history is the primary recovery mechanism. Do not use destructive resets or
force-pushes to repair a disputed state.

If the live tree is damaged:

1. Preserve the damaged tree and record its commit identity.
2. Clone the repository at the required commit into a new directory.
3. Run the cold-rebuild checks.
4. Use the portability ZIP only to compare or restore process tools.
5. Restore content from Git history through a reviewed commit, not by copying
   generated hosted outputs back into the repository.

`MASTER.md` is data, not an operational model input. Recovery must preserve its
exclusion from the published site. It is not duplicated in portability.
