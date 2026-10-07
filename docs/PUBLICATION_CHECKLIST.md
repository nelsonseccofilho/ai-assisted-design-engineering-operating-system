# PUBLICATION CHECKLIST

Use this checklist before publishing or updating a public copy of the framework.

## 1. Project identity

Search for and remove:

- real client/company names;
- real stakeholder names;
- real product codenames;
- real Work Package names;
- real journey names.

## 2. URLs and identifiers

Search for and remove:

- private Figma URLs;
- file keys;
- node IDs;
- private Drive/Docs links;
- ticket links;
- internal repository links;
- private hostnames.

## 3. Evidence and history

Search for and remove:

- proprietary requirements;
- copied stakeholder comments;
- internal change IDs;
- screenshots containing confidential material;
- transcripts or recordings;
- historical project exports.

## 4. Secrets

Search for and remove:

- tokens;
- API keys;
- OAuth secrets;
- passwords;
- private environment values.

## 5. Runtime files

Confirm these are not tracked:

```text
PROJECT_CONTEXT.local.md
HANDOFF_CURRENT.local.md
*.private.md
.env
```

## 6. Examples

Examples must be explicitly fictional or use obvious placeholders.

Never “anonymize” a real project by changing only the company name while leaving unique file names, URLs, taxonomy, or internal identifiers intact.

## 7. Final repository scan

Run a full-text search for known project terms before every public release.

The public repository should contain only:

- generic operating rules;
- templates;
- fictional examples;
- public documentation.

## Licensing check

Before publishing a release:

- [ ] `LICENSE` is present and unchanged except for permitted required notices.
- [ ] `LICENSE-DOCS.md` correctly identifies the documentation scope.
- [ ] `COMMERCIAL-LICENSE.md` does not accidentally grant commercial rights.
- [ ] README describes the project as noncommercial/source-available rather than OSI Open Source.
- [ ] Copyright holder and year are correct.
- [ ] No third-party material is relicensed unless the project has the right to do so.


## Decision documentation check

Before publishing a release:

- [ ] Every significant framework decision has a decision record.
- [ ] New ADRs are indexed in `DECISION_LOG.md`.
- [ ] Superseded decisions remain historically visible.
- [ ] Changelog entries reference the decision when relevant.
- [ ] Commits that implement, change, supersede, or operationalize significant decisions reference the corresponding Decision ID (for example, `Decision: ADR-0013`).
- [ ] No confidential project/client decision record is included in the public release.

## Owner history and package QA

- [ ] Identify every actually mutated owner separately from read-only evidence dependencies.
- [ ] Every significant mutation has an owner-scoped persistent record; missing history is established before FINAL.
- [ ] Each owner history location and namespace is registered in project context.
- [ ] Multi-artifact records link each other; shared libraries do not log consumer-only changes.
- [ ] Evidence-only consumer inspection and library references create no spurious records.
- [ ] No central fallback log is used.
- [ ] Historical ownership corrections retain the original as archived/pointer evidence and link the new canonical copy append-only.
- [ ] Decisions, owner records, Git implementation and Handoff/workstream links agree; chat memory is not persistent history.
- [ ] Startup loads Master, context and handoff, resolves owner governance/records, inspects current state and only then mutates.
- [ ] Run `python scripts/validate_framework.py`; inspect templates and generic examples manually.


## Hosted CI disposition

Before releasing with a non-executing hosted CI gate:

- [ ] Confirm the job had no assigned runner and no executed steps/logs.
- [ ] Confirm equivalent static/local QA passed.
- [ ] Confirm required live pilots passed.
- [ ] Confirm privacy/secret scans passed.
- [ ] Record the governance decision and evidence.
- [ ] Describe the gate as `DISPOSITIONED_INFRASTRUCTURE`, not `PASS`.
- [ ] Keep a future real hosted run as follow-up evidence.
