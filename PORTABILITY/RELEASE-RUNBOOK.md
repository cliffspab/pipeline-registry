# Release runbook

1. Inspect `git status`, `git diff --check` and the local/origin commit
   identity.
2. Validate all assembler outputs, deployments, custom parts and Directory
   copies in an isolated candidate.
3. If process machinery or portability documents changed, rebuild the
   tools-only ZIP. Do not touch portability for a content-only commit.
4. If `origin/main` has advanced, stop. Combine and revalidate before any
   commit; do not rebase a validated payload after the fact.
5. Commit the exact reviewed payload with a clear message and push.
6. Confirm local HEAD equals `origin/main`.
7. Confirm the **Hosted builds from master** workflow succeeds.
8. Verify the hosted edition, Blueprint, skills and Directory copies, and
   verify that the master itself is not hosted.

There is no cloud-mirror or Shift publication stage.

GitHub's commit page is the exact file-and-line change record. No parallel
change ledger is maintained in the repository.
