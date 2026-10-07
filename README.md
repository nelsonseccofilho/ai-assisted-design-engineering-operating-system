# AI-Assisted Design Engineering Operating System

> A versioned operating framework for persistent, evidence-driven collaboration between Product Designers and AI agents across Product Design, UI, Design Systems, Figma, QA, documentation and design operations.

**Status:** Experimental / evolving  
**Framework version:** 3.6.0  
**Canonical operating contract:** `PROMPT_OPERACIONAL_MASTER.md`

## What this is

AI can already inspect interfaces, compare variants, generate UI, reason about Design Systems, help with implementation and automate repetitive work.

The harder problem begins when AI stops being used for isolated prompts and starts participating in real product work across multiple days, chats, files, stakeholders and tools:

> **How do we preserve intent, context, evidence, ownership, quality and continuity when the AI session itself is temporary?**

This repository treats AI-assisted design work less like a conversation and more like an operational system.

It provides explicit sources of truth, a persistent Project Runtime, Workstreams, Sessions, Decisions, evidence provenance, mutation ownership, QA, reporting and handoff rules.

It is intentionally organization-agnostic. Real client names, stakeholder identities, private Figma URLs, proprietary transcripts and project history do not belong in this public repository.

## The problems it addresses

Without a durable operating model, AI-assisted design work can drift in predictable ways:

- **Context loss** — a new chat does not know what the previous one validated.
- **Method repetition** — the human repeatedly re-explains the same operating rules.
- **Design drift** — a proposed improvement silently changes approved behavior or semantics.
- **Design System drift** — local patterns are duplicated or promoted before they are mature.
- **Evidence decay** — an old reference outranks a newer decision, or inference becomes “fact”.
- **Conversation state ≠ tool state** — a handoff says one thing while the artifact has changed.
- **Parallel-work ambiguity** — multiple humans/agents touch related scope without explicit ownership.
- **Weak provenance** — requirements are disconnected from the meeting, ticket or approval that produced them.
- **Tool failure becoming workflow failure** — one unavailable integration stops useful analysis.
- **Cognitive overload** — the AI returns more process narration than the human needs to decide and continue.

The operating contract reduces these problems through explicit context, provenance, risk classification, scope control, QA and compact human-facing reporting:

`STATUS → EVIDENCE → ACTION → QA → NEXT`

## Who this is for

This framework is useful for:

- Product Designers using AI across long-running product work;
- Design Engineers working between design and implementation;
- Design System teams introducing agentic workflows;
- consultants who need repeatable project onboarding and traceability;
- teams using Figma or similar tools with automation/MCP integrations;
- anyone who needs AI work to survive beyond one conversation.

## Core principles

### Human accountability

AI can inspect, propose, mutate and validate within governed scope. Product judgment, approval interpretation and final accountability remain human responsibilities.

### Evidence before inference

The framework distinguishes:

`FACT ≠ INFERENCE ≠ ASSUMPTION`

Primary evidence outranks convenience memory.

### Parity before evolution

When reconstructing or repairing an approved artifact:

`PARITY BEFORE UX EVOLUTION`

Do not modernize, simplify or “improve” behavior before reproducing what is actually approved.

### Reuse before creation

`REUSE → COMPOSE → EVOLVE → CREATE`

Prefer canonical Design System components and patterns before inventing new ones.

### Mutation-owned history

`THE FILE / ARTIFACT THAT OWNS THE MUTATION OWNS THE CHANGE RECORD`

Read-only dependencies do not become central logs for consumer changes.

### Persistent continuity

Chat/model memory is useful but non-authoritative. Durable state belongs in versioned project/runtime records.

## System model

```text
Operating System
= how the work is governed

Project Runtime
= where project operational state persists

Primary evidence
= where requirements / approvals originate

Canonical Design System
= shared system truth

Current artifact
= current implementation / design truth

AI session
= temporary executor
```

## Architecture

### 1. Operating Model

`PROMPT_OPERACIONAL_MASTER.md`

Defines reusable rules for:

- role and responsibility boundaries;
- evidence hierarchy;
- fact / inference / assumption;
- Design System usage;
- scope discipline;
- risk classification;
- preflight / postflight;
- QA and accessibility;
- documentation and handoff;
- runtime/session startup;
- completion criteria.

### 2. Project Runtime

`runtime/`

A deployable project-specific operational memory. A private project instance populates the same canonical runtime structure with real context, evidence, operators, Sessions, Workstreams and Decisions.

The runtime is authoritative for operational continuity, not for current artifact state or primary evidence.

### 3. Current artifact and evidence sources

Design tools, repositories, tickets, recordings, transcripts, specifications and stakeholder approvals remain authoritative at their original sources.

The runtime records durable mappings and continuity around them.

## From stakeholder meeting to traceable evidence

A meeting should not become a requirement merely because it was transcribed.

The generic evidence pipeline is:

```text
stakeholder meeting
        ↓
local recording (for example OBS Studio)
        ↓
raw audio/video
        ↓
local transcription (for example WhisperX)
        ↓
diarized machine-readable transcript
        ↓
reviewed Evidence ID + metadata
        ↓
requirement / decision
        ↓
Workstream / implementation
        ↓
owner-scoped Change History
        ↓
QA / status
```

The key distinction is:

```text
recording ≠ transcript
transcript ≠ approved requirement
approved requirement ≠ implementation
implementation ≠ validated completion
```

Each transition should preserve provenance.

See:

- [Evidence ingestion](docs/EVIDENCE_INGESTION.md)
- [Local transcription setup](docs/LOCAL_TRANSCRIPTION_SETUP.md)
- [Runtime evidence archive](runtime/evidence/README.md)

## Quick start

### Prerequisites

For the framework itself:

- Git;
- Python 3.9+ for the dependency-free QA/synchronization scripts.

No package installation is required to read or apply the operating model.

### Clone

```bash
git clone https://github.com/nelsonseccofilho/ai-assisted-design-engineering-operating-system.git
cd ai-assisted-design-engineering-operating-system
```

### Validate the framework

```bash
python scripts/validate_framework.py
python scripts/test_runtime_sync.py
python scripts/runtime_sync.py --framework .
```

The validators use the Python standard library only.

### Start using the method

For a lightweight first contact, read:

1. `START_CHAT.md`
2. `PROMPT_OPERACIONAL_MASTER.md`
3. `docs/RATIONALE.md`

For persistent work, create a separate private Project Runtime from `runtime/`.

## Starting a new AI chat

The canonical persistent entrypoint is:

`runtime/00_START_CHAT.md`

A new chat must first classify the startup intent:

1. `CONTINUE_WORKSTREAM` — resume an existing objective;
2. `START_NEW_WORKSTREAM` — start a new task, journey, flow or independent objective inside the same project;
3. `START_NEW_PROJECT` — create a separate private runtime for a different project/client/product.

Example — new work inside an existing project:

> Load the Project Runtime from `main` using `runtime/00_START_CHAT.md`. Intent: `START_NEW_WORKSTREAM`. New work: <describe it>. Do not inherit another Workstream's NEXT ACTION by default. Check scope overlap, initialize the new Workstream and report recovered state before mutation.

Example — completely separate project:

> Intent: `START_NEW_PROJECT`. Create a new private Project Runtime from the generic `runtime/` package. Do not copy populated Sessions, evidence, Reports, Decisions or Workstreams from another project.

## Optional local meeting transcription

Local transcription is an **optional evidence-ingestion capability**, not a requirement for using this framework.

A common workflow uses:

- OBS Studio (or another approved recorder) for local meeting capture;
- WhisperX for local speech-to-text, word-level alignment and optional speaker diarization;
- JSON output for deterministic review and downstream evidence mapping.

Current WhisperX upstream recommends installation from PyPI:

```bash
pip install whisperx
```

CPU example:

```powershell
whisperx ".\stakeholder-session.mkv" --model medium --device cpu --compute_type int8 --diarize --output_dir ".\transcriptions" --output_format json --language pt
```

GPU acceleration is optional. Current WhisperX documentation describes CUDA 12.8 for its GPU path and requires a Hugging Face read token plus acceptance of the relevant pyannote model terms for speaker diarization.

Do not put credentials directly in scripts or repositories.

See [Local transcription setup](docs/LOCAL_TRANSCRIPTION_SETUP.md) for the complete setup and validation flow.

## Evidence storage policy

Raw recordings are usually heavyweight and may contain sensitive material. The generic policy is:

```text
raw recording
→ private/local approved storage
→ not committed to public Git

approved lightweight transcript / derived evidence
→ private Project Runtime when project policy allows

metadata / Evidence ID
→ versioned for provenance
```

A public framework must never contain real client recordings or proprietary transcripts.

## Documentation ownership

Durable documentation is classified before persistence:

- `FRAMEWORK_OWNED` — reusable method, framework ADRs, framework CI/release history, generic templates/schemas/scripts/QA;
- `PROJECT_OWNED` — project/client context, stakeholder requirements, private evidence, project Decisions and populated runtime history;
- `SHARED_CONTRACT` — framework-authored reusable contract consumed by a pinned runtime;
- `CROSS_REPO_REFERENCE` — reference between canonical owners without duplicated history.

See:

- [ADR-0023](docs/decisions/ADR-0023-documentation-ownership-boundary.md)
- [Documentation Ownership contract](runtime/docs/contracts/DOCUMENTATION_OWNERSHIP.md)

## Project Runtime topology

```text
runtime/
├── operators/      # WHO
├── sessions/       # WHICH CHAT / WHEN
├── workstreams/    # WHAT CONTINUES
├── reports/        # WHAT WAS COMMUNICATED
├── evidence/       # APPROVED LIGHTWEIGHT EVIDENCE
├── docs/decisions/ # WHY
├── compat/         # governed compatibility aliases
└── scripts/        # runtime validation / synchronization
```

Workstreams are independent of operator identity. Sessions record which chat/operator executed work. Handoffs preserve the current safe continuation point.

## Daily reports

A Project Runtime can generate concise human-facing status reports from persistent evidence.

The generic model supports:

- per-operator reporting cursors;
- DRAFT vs SENT distinction;
- project-configurable languages;
- worked / next / blockers-help summaries;
- optional mandatory daily mode.

Recommended command pattern:

`<operator_alias_lower>_report`

and confirmation after actual delivery:

`<operator_alias_lower>_report_sent`

See [Operator Daily Reports](docs/OPERATOR_DAILY_REPORTS.md).

## Repository structure

```text
ai-assisted-design-engineering-operating-system/
├── README.md
├── START_CHAT.md
├── PROMPT_OPERACIONAL_MASTER.md
├── prompt-operacional.json
├── PROJECT_CONTEXT_TEMPLATE.md
├── HANDOFF_TEMPLATE.md
├── DECISION_LOG.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── LICENSE-DOCS.md
├── COMMERCIAL-LICENSE.md
├── runtime/
│   ├── 00_START_CHAT.md
│   ├── package.index.json
│   ├── operators/
│   ├── sessions/
│   ├── workstreams/
│   ├── reports/
│   ├── evidence/
│   ├── docs/
│   ├── compat/
│   └── scripts/
├── scripts/
├── examples/
└── docs/
    ├── RATIONALE.md
    ├── PROJECT_RUNTIME.md
    ├── EVIDENCE_INGESTION.md
    ├── LOCAL_TRANSCRIPTION_SETUP.md
    ├── FRAMEWORK_RUNTIME_SYNC.md
    ├── CHANGE_RECORD_OWNERSHIP.md
    ├── DOCUMENTATION_OWNERSHIP.md
    └── decisions/
```

## Privacy and security

The public repository contains the method, not real project context.

Never publish:

- client/stakeholder identities from private projects;
- private Figma file keys or node IDs;
- credentials, tokens, OAuth secrets or private keys;
- raw meeting recordings;
- proprietary transcripts;
- populated private Sessions, Reports or operator profiles.

See [SECURITY.md](SECURITY.md).

## Validation and current maturity

Framework 3.6.0 is the current released operating contract.

Validated capabilities include:

- canonical Project Runtime structure;
- cross-chat bootstrap/state recovery;
- live-artifact reconciliation in a private adopter;
- zero-chat startup intents;
- real Daily Report DRAFT → external send → SENT confirmation;
- documentation ownership and public/private boundaries;
- privacy/secret scanning and local static QA.

Hosted CI is currently documented under ADR-0022 as `DISPOSITIONED_INFRASTRUCTURE`, **not** as CI PASS. The local validation scripts remain available independently of hosted CI.

This is a living framework, not a finished industry standard.

## Licensing

This project uses a noncommercial public licensing model:

- framework/software-like materials: **PolyForm Noncommercial License 1.0.0**;
- documentation/editorial materials: **CC BY-NC 4.0**;
- commercial use: reserved to the copyright holder and available only through a separate written license.

Copyright © 2026 **Nelson Secco Filho**.

See:

- [LICENSE](LICENSE)
- [LICENSE-DOCS.md](LICENSE-DOCS.md)
- [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)

This repository is source-available for noncommercial use and should not be described as OSI Open Source.

## About the author

**Nelson Secco Filho** is a Senior Product Designer and UX Consultant working at the intersection of Design, Product and Engineering.

His public portfolio describes a hands-on practice focused on complex digital products, UX strategy, Product Discovery, Design Systems and AI-assisted Product Design, supported by a background in software development.

This operating system grew from the same hypothesis demonstrated in his portfolio work: AI can accelerate analysis, prototyping, implementation and validation, while decisions, critical review and quality criteria remain human responsibilities.

- Portfolio: https://nelsonsecco.netlify.app/
- LinkedIn: https://www.linkedin.com/in/nelsonseccofilho/
- GitHub: https://github.com/nelsonseccofilho

## Português — resumo

Este repositório é um framework versionado para colaboração persistente e orientada por evidências entre Product Designers e agentes de IA.

Ele resolve principalmente perda de contexto entre chats, drift de design, ambiguidade de ownership, degradação de evidências e falta de rastreabilidade entre pedido → decisão → implementação → QA.

O framework público contém **o método**. Contexto real de cliente, transcrições, evidências, operadores e histórico operacional pertencem a Project Runtimes privados.

Para começar:

1. leia `START_CHAT.md`;
2. leia `PROMPT_OPERACIONAL_MASTER.md`;
3. para trabalho persistente, use `runtime/00_START_CHAT.md`;
4. para captura/transcrição de reuniões, consulte `docs/EVIDENCE_INGESTION.md` e `docs/LOCAL_TRANSCRIPTION_SETUP.md`.
