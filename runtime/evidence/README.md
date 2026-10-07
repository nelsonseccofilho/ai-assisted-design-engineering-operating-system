# Evidence archive

The evidence archive stores lightweight approved evidence and metadata for deterministic retrieval inside a Project Runtime.

## Principle

```text
recording ≠ transcript
transcript ≠ approved requirement
approved requirement ≠ implementation
implementation ≠ validated completion
```

Preserve provenance across every transition.

## Recommended structure

```text
evidence/
└── <category>/
    └── <EVIDENCE-ID>/
        ├── EVIDENCE_METADATA.md
        └── <approved lightweight evidence when policy allows>
```

Example categories:
- `stakeholder-meetings/`
- `requirements/`
- `research/`
- `approvals/`

## Raw recordings

Heavyweight meeting recordings should normally remain in approved private/local storage rather than Git.

Do not store:
- secrets;
- credentials;
- unapproved raw exports;
- heavyweight recordings.

## Transcripts

A transcript can be stored only when project policy permits it.

Before treating a transcript as durable evidence:
- retain its recording/source relationship;
- record date, language and transcription profile;
- record diarization/review status;
- use a stable Evidence ID;
- link derived requirements/Decisions/Workstreams.

## Metadata

Use `evidence/_template/EVIDENCE_METADATA.md`.

A project may additionally capture fingerprints such as SHA-256 for the original recording and transcript so evidence can be matched to its source without versioning the heavyweight recording itself.

## Generic ingestion guidance

Canonical framework documentation:
- https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/blob/main/docs/EVIDENCE_INGESTION.md
- https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system/blob/main/docs/LOCAL_TRANSCRIPTION_SETUP.md

Project-specific evidence locations, operator profiles and real stakeholder context remain PROJECT_OWNED in the private runtime.
