# Operator Daily Reports

Operator Daily Reports are a Project Runtime capability for generating human-facing status updates from persistent operational evidence.

## Why

The runtime may know what happened across many chats, but a human should not have to reconstruct that history manually for a team status request.

## Generic commands

Recommended:

`<operator_alias_lower>_report`

`<operator_alias_lower>_report_sent`

Projects may configure other aliases.

## Source order

1. last confirmed reporting cursor;
2. Session Records;
3. persistent mutation / Git records;
4. current Workstream handoff/state;
5. explicit blockers, dependencies, help requests.

Chat/model memory is not sufficient as the sole source.

## States

- NOT_DUE
- DUE
- DRAFT
- SENT
- WAIVED
- SUPERSEDED

DRAFT never advances the cursor.

SENT advances the cursor.

WAIVED requires a human reason.

## Mandatory mode

The framework does not assume every project requires daily status reports.

A Project Runtime may set:

`daily_operator_reports.required = true`

When enabled, an operator with material activity must end the reporting day as SENT or WAIVED.

## Output

Recommended semantic groups:

- worked since last update;
- planned today / next;
- blockers or help needed.

Languages are project-configured.

Prefer outcomes over technical IDs.

Do not invent blockers.

## Persistence

Recommended:

`reports/daily/<OPERATOR_ALIAS>/state.json`

`reports/daily/<OPERATOR_ALIAS>/<YYYY>/<MM>/<YYYY-MM-DD>_<HHmm>_daily-report.md`

## Reporting coverage and confirmation

Freeze an offset-aware `interval_end` when generating a DRAFT. On confirmed sending, set `last_confirmed_report_at` to that report's `interval_end`, not its `sent_at`; store the actual send time separately as `last_sent_at`. Activity after generation remains eligible for the next report. Read material deltas in OPEN Session Records as well as new records; a session's creation date alone cannot select its later updates.

Confirmation requires READ_WRITE, an existing operator-matching DRAFT and evidence of actual sending. Invoking the sent command is the human's confirmation; ask only if that intent or the draft is ambiguous. Reject missing, superseded or already confirmed drafts without moving the cursor. Repeated confirmation is idempotent. Refreshing a draft preserves the previous draft as SUPERSEDED. WAIVED records the reporting date, human, time and reason, and does not advance the cursor. Day rollover recomputes DUE from material activity; absence of activity remains NOT_DUE.
