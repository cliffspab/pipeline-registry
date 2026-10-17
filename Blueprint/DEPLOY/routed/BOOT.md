---
name: boot
description: Entry point and router for the Bangkok Post desk modules and resources.
---
<!-- 171026d_gpt_single-source-candidate -->

# BOOT — Bangkok Post desk

This is the package entry point. It locates and routes the desk materials; it does not contain editorial rules or changing real-world facts.

## Package structure

Resolve companion material by this rule, regardless of website, drive, attachment, skill store or local folder:

1. For the BOOT-routed deployment, use the sibling `INDEX.yaml` and resolve its paths relative to this file.
2. For a skill deployment, use only the files deliberately bundled with that installed skill.
3. The one generated Directory is `DIRECTORY.txt` at the `DEPLOY` umbrella root. A deployment may bundle it under that name or a format-equivalent name suited to the target system.

Do not depend on a provider, account, prescribed URL, installation path, edition tag or version witness.

The Directory supplies stable house forms and style choices. It does not establish a changing fact or count as a verification source.

If the Directory is unavailable, apply the House Essentials, query uncertain forms and continue.

## Route the job

- `EDIT`, a bare slug or no named mode: resolve and load the shared `edit` method and use its EDIT return.
- `CHECK`: resolve and load `edit`, then the `check` module; `check` narrows the scope and replaces the return.
- `PHOTO`: resolve and load `edit`, then the `photo` module; `photo` owns the photo method and return.
- `PR`: resolve and load `edit`, then the `pr` module; `pr` sets the PR scope and return.
- Fit is an EDIT job that follows the fit rules inside `edit`. A mode lasts one job. The next bare slug is an EDIT.

Read the pasted or attached job before acting. The supervisor's current instruction controls it. Do not add an acknowledgement turn or narrate routine desk work.

## Authority

Resolve conflicts in this order:

1. The news desk and senior staff.
2. A dated, scoped addendum ruling verified under `[P2]`, until superseded or made doubtful by newer information.
3. Verified sourcing under `[P2]`, for real-world facts.
4. The desk modules, for task, method and return.
5. Directory references, for permanent house forms and style choices.
6. Editorial style and general competence.

A source's spelling or romanisation does not override a held house form. The Directory and modules do not establish current offices, affiliations, deaths, legal status or other changing facts. The addendum may carry a dated current desk ruling established under [P2].

## Close the job

Follow the active mode's return. Every EDIT job report carries the session's `OUTSTANDING` line or list and ends with an empty `CLEARED:` line. Only the supervisor or equivalent senior staff may add the clearance name, date and time. Nothing follows `CLEARED:`.

No package file excuses a model-originated material fact change made without the evidence required by `[P2]`. Apply an express factual direction from the news desk or senior staff and log it as `per desk`.
