# Guarded release and distribution

## Candidate

For substantive machinery changes, work in an isolated candidate. Prove the
valid source still generates byte-identical outputs, test the new failure
guards, rebuild the Word volume if required and inspect the complete diff.
Record the user-facing change, edition reasoning and exact pending payload.

## Publication

The supervisor runs `push.bat`. Its preflight is read-only and displays
unstaged changes, staged changes, untracked files, unpublished commits and
`COMMITS-PENDING.md`. Typing `PUSH` authorises that payload.

The script then:

1. archives pending entries and stages the displayed tree;
2. commits if necessary;
3. fetches again and aborts if upstream advanced;
4. pushes without rebasing;
5. proves local HEAD equals `origin/main`;
6. waits for successful GitHub validation;
7. extracts `Blueprint/` from that exact commit;
8. copies and verifies it on pCloud, Google Drive and OneDrive;
9. backs up the committed portability ZIP, manifest and snapshot on OneDrive;
10. writes `.publication/last.json`.

It stops on the first failed guard. It never runs `rclone sync`, removes
remote extras, deletes `.git/index.lock` or rebases an already validated tree.

## Routine evidence

Successful execution should require only the final PASS line and local receipt.
Inspect detailed logs only after a failure. Multi-model mechanism audits are for
material mechanism changes, not routine content editions.
