# Contributing

Thank you for helping improve the AI-Assisted Design Engineering Operating System.

## Commit convention

All commits must follow **Conventional Commits 1.0.0**:

https://www.conventionalcommits.org/en/v1.0.0/

This convention is part of the operating contract for this framework and for persistent project runtimes that adopt it, unless a stricter repository policy is explicitly documented.

Format:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

Examples:

```text
docs(rationale): clarify persistent-context problem
feat(templates): add project decision log template
fix(master): correct evidence precedence rule
chore(release): prepare v3.4.0
feat(governance)!: change decision-record contract

BREAKING CHANGE: project decision logs now require a stable decision ID
```

### Preferred types

- `feat` — new capability or feature
- `fix` — correction
- `docs` — documentation-only change
- `refactor` — restructuring without changing intended behavior
- `test` — validation/test changes
- `build` — build or packaging changes
- `ci` — continuous integration changes
- `chore` — repository maintenance
- `perf` — performance improvement
- `style` — formatting/style-only changes
- `revert` — revert of a previous change

### Suggested scopes

Use a scope when it improves clarity:

- `master`
- `governance`
- `decisions`
- `templates`
- `examples`
- `licensing`
- `release`
- `docs`

### Commit discipline

- Prefer one coherent logical change per commit.
- Do not use vague descriptions such as `update files` or `changes`.
- Mark breaking changes explicitly with `!` or a `BREAKING CHANGE:` footer.
- Do not expose private client/project information in commit messages.
- Significant decisions must also have a persistent decision record; a commit message does not replace an ADR.
- A commit that implements, changes, supersedes, or operationalizes a significant decision must reference the corresponding Decision ID in its body or footer.
- Preferred form: `Decision: ADR-XXXX`.
- Routine commits that do not implement a significant decision do not require an ADR reference.

## Decision governance

See:

- `DECISION_LOG.md`
- `docs/decisions/`
- `docs/decisions/ADR_TEMPLATE.md`

A significant decision is not complete until its rationale is documented.

### Decision traceability

For a significant change, use this chain:

```text
ADR / Decision Record
        ↓
Conventional Commit
        ↓
Changelog / Release
```

Example:

```text
docs(governance): link significant commits to ADRs

Decision: ADR-0013
```
