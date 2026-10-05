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
- [ ] No confidential project/client decision record is included in the public release.
