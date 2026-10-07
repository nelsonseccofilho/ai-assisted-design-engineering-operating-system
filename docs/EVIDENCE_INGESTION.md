# Evidence ingestion

Evidence ingestion defines how source material becomes durable, traceable project evidence without collapsing distinct stages into one another.

## Principle

```text
recording ≠ transcript
transcript ≠ approved requirement
approved requirement ≠ implementation
implementation ≠ validated completion
```

Each transition must preserve provenance.

## Typical stakeholder-meeting flow

```text
stakeholder meeting
        ↓
approved local recording
        ↓
raw audio/video
        ↓
local transcription
        ↓
speaker diarization / timestamps
        ↓
human review
        ↓
Evidence ID + metadata
        ↓
requirement / decision mapping
        ↓
Workstream
        ↓
artifact mutation
        ↓
Change History
        ↓
QA / status
```

OBS Studio and WhisperX are examples of tools that can support this workflow. They are not mandatory dependencies of the operating framework.

## Source classes

### Raw recording

The original meeting capture.

Treat it as sensitive primary material. It may contain personal data, confidential discussion or irrelevant conversation.

Recommended default:
- private/local approved storage;
- do not commit to public Git;
- do not copy into a Project Runtime unless project policy explicitly permits it.

### Transcript

A machine-generated or human-edited representation of the recording.

A transcript is evidence, not automatically an approved requirement.

Preserve:
- recording relationship;
- date/time;
- language;
- transcription tool/profile;
- diarization status;
- review status.

### Evidence record

A durable project record that can be retrieved deterministically.

Recommended fields:
- Evidence ID;
- date;
- source type;
- meeting / source description;
- storage location;
- recording fingerprint when available;
- transcript fingerprint when available;
- review status;
- related stakeholders;
- related requirements;
- related Decisions;
- related Workstreams;
- related artifact/change records.

### Requirement / decision

Requirements and decisions are interpretations or approvals derived from evidence.

Do not silently promote every spoken sentence to a requirement.

Classify, when useful:
- explicit stakeholder request;
- approval;
- business rule;
- open question;
- design inference;
- implementation constraint;
- superseded statement.

## Evidence IDs

Use stable IDs suitable for cross-reference, for example:

`EVD-YYYY-MM-DD`

or a project-specific extension such as:

`EVD-2026-10-07-STAKEHOLDER-01`

The Project Runtime evidence index should map each ID to its durable source.

## Metadata example

```text
Evidence ID: EVD-2026-10-07-01
Date: 2026-10-07
Type: stakeholder meeting transcript
Recording tool: OBS Studio
Transcription tool: WhisperX
Language: pt
Diarization: enabled
Recording location: <private location>
Recording SHA-256: <optional fingerprint>
Transcript location: <private runtime or approved store>
Transcript SHA-256: <optional fingerprint>
Review status: REVIEWED / UNREVIEWED
Related requirements: REQ-...
Related Workstreams: WS-...
Related changes: <artifact change IDs>
```

## Human review

Automatic transcription can be wrong.

WhisperX itself documents limitations including imperfect diarization and problems with overlapping speech. A transcript therefore should not be treated as flawless source text.

Review the passages that materially affect:
- scope;
- approval;
- legal/compliance interpretation;
- business rules;
- user-impacting behavior;
- irreversible or high-risk changes.

## Supersession

Older evidence remains historical evidence.

If newer primary evidence changes a prior significant decision:
1. preserve the older evidence;
2. create or update the appropriate Decision record;
3. mark the prior decision as superseded when applicable;
4. update Workstream/Handoff state;
5. do not rewrite history to make the old evidence appear as though it never existed.

## Public/private boundary

The public framework owns this generic ingestion method.

Real recordings, transcripts, stakeholder identities, artifact IDs and project-specific evidence are PROJECT_OWNED and belong in the adopting private runtime or another governed private source.

See:
- `runtime/evidence/README.md`
- `runtime/docs/contracts/DOCUMENTATION_OWNERSHIP.md`
- `docs/LOCAL_TRANSCRIPTION_SETUP.md`
