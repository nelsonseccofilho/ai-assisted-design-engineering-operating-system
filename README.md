# AI-Assisted Design Engineering Operating System

> A personal research framework for persistent, evidence-driven collaboration between designers and AI agents across Product Design, UI, Design Systems, Figma, QA, and design operations.

**Status:** Experimental / evolving  
**Framework version:** 3.4.0  
**Canonical operating contract:** `PROMPT_OPERACIONAL_MASTER.md`

[English](#english) · [Português](#português)

---

# English

## Why this exists

AI can already help designers inspect files, reason about interfaces, generate and modify UI, work with Design Systems, review accessibility, and automate parts of implementation.

The difficult part is no longer only **what an AI can do inside one conversation**.

The harder operational problem is:

> **How do we preserve quality, context, evidence, governance, and continuity across many AI sessions, tools, files, stakeholders, and days of work?**

Without an explicit operating system, the human becomes the memory layer.

This repository explores a reusable workflow for solving that problem.

It is a **personal research project and an evolving consulting framework**. It is intentionally organization-agnostic: no client, company, stakeholder, Design System, or production Figma URL is hardcoded into the public framework.

---

## The daily pain

A designer working deeply with AI may repeatedly face:

1. **Context loss** — a new session does not know what the previous one validated.
2. **Method repetition** — the human has to explain the same operating rules again.
3. **Design drift** — something looks better but silently changes approved behavior or semantics.
4. **Design System drift** — AI creates duplicates, changes shared tokens, or promotes local patterns too early.
5. **Evidence decay** — an old reference overrides a newer decision, or an assumption becomes “fact”.
6. **Conversation state ≠ tool state** — a handoff says one thing while the design file has changed.
7. **Tool failure becoming workflow failure** — one unavailable integration stops otherwise useful analysis.
8. **Cognitive overload** — the AI returns more explanation than the human needs to decide and continue.

The operating model reduces these problems through explicit context, provenance, risk classification, QA, handoff, and a compact human-facing response contract:

`STATUS → EVIDENCE → ACTION → QA → NEXT`

---

## What is “AI-Assisted Design Engineering”?

**Design Engineer** is a useful established direction for work that crosses product thinking, UI craft, Design Systems, prototyping, and implementation.

This framework uses **AI-Assisted Design Engineering** to describe the practice of adding AI agents to that operational loop:

`understand → inspect → compare → decide → mutate → validate → document → hand off`

The AI is not only generating UI. It is participating in a governed workflow while the human keeps responsibility for product judgment, intent, and final accountability.

The exact job title is less important than the operating model.

---

## Architecture

The framework separates three layers:

### 1. Operating Model — stable

`PROMPT_OPERACIONAL_MASTER.md`

Defines **how the AI should work**:

- role and responsibilities;
- evidence hierarchy;
- fact / inference / assumption;
- Design System rules;
- scope discipline;
- risk classification;
- preflight and postflight;
- QA;
- accessibility;
- documentation;
- first-run onboarding;
- session startup;
- handoff;
- completion criteria.

### 2. Project Context — persistent but project-specific

Public template:

`PROJECT_CONTEXT_TEMPLATE.md`

Runtime/private file:

`PROJECT_CONTEXT.local.md`

Defines **where and with whom the work happens**, for example:

- organization;
- product/project;
- stakeholder / decision-maker;
- work package / initiative;
- journey / flow;
- Design System / UI Kit name and URL;
- primary work file name and URL;
- governance location;
- evidence locations.

### 3. Current Work State — volatile

Public template:

`HANDOFF_TEMPLATE.md`

Runtime/private file:

`HANDOFF_CURRENT.local.md`

Defines **what is happening now**:

- objective;
- current scope;
- references;
- decisions;
- completed work;
- pending work;
- QA status;
- known risks;
- last action;
- exact next action.

---

## Persistent Project Runtime

For long-running work, the framework supports a **Project Runtime**: a project-specific, versioned operational memory that survives chat boundaries.

It is the place where a project can persist governance, decisions, Workstreams, handoffs, deterministic state, operator identities and Session Records.

It is **not** the universal source of truth:

- requirements remain authoritative at their primary evidence source;
- the current inspected artifact remains authoritative for current artifact state;
- the canonical Design System remains authoritative for shared system state;
- the Project Runtime is authoritative for operational continuity;
- chat/model memory is convenience only.

A useful model:

```text
Operating System = how we work
Project Runtime  = where project operational state persists
Artifact tools   = where current design / implementation lives
AI session       = temporary executor
```

See [Project Runtime](docs/PROJECT_RUNTIME.md).

## First run

The framework starts in **generic mode**.

It must not assume a company, stakeholder, Design System, project, or file.

When no project context exists, the AI asks for only the minimum useful context and briefly explains why it matters.

Recommended initial fields:

| Field | Purpose | Required initially? |
|---|---|---:|
| Organization / client | Project identity and separation | No |
| Product / project | Defines the product context | Yes |
| Primary stakeholder / decision-maker | Helps classify approval authority | Yes |
| Work Package / initiative | Limits scope when the organization uses one | No |
| Journey / flow | Defines the current product area | Yes |
| Design System / UI Kit name | Identifies canonical design source | Conditional |
| Design System / UI Kit URL | Allows direct inspection | Conditional |
| Work file name | Identifies the active file | Yes before tool execution |
| Work file URL | Allows direct inspection | Yes before tool execution |

Additional context is collected **just in time**, not all at once.

Examples:

- approved reference / source of truth;
- Local Components;
- governance documentation;
- recordings / transcripts;
- tickets or requirements;
- implementation constraints.

> **Context should be collected just in time, not all at once.**

---

## Privacy model

The public repository contains **the method**, not real project context.

These files are intentionally ignored by Git:

```text
PROJECT_CONTEXT.local.md
HANDOFF_CURRENT.local.md
*.private.md
.env
```

Never hardcode real client/company names, stakeholder names, internal Figma URLs, private Design Systems, credentials, or proprietary evidence into the canonical framework.

Use the local runtime files for those values.

---

## Design rationale / Racional do framework

For the reasoning behind the architecture, the daily problems this workflow is intended to solve, and the product/consulting hypothesis behind the project, see:

[`docs/RATIONALE.md`](docs/RATIONALE.md)

Esse documento explica por que o framework existe, quais dores operacionais ele tenta reduzir, por que o contexto foi separado em Operating Model / Project Context / Handoff e como isso pode evoluir como prática, serviço de consultoria ou produto.

## Licensing

This project uses a **noncommercial public licensing model**.

- Framework, prompt-system, schemas, automation and software-like materials: **PolyForm Noncommercial License 1.0.0**
- Documentation and editorial materials: **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**
- Commercial use: **reserved to the copyright holder and available only through a separate written commercial license**

Copyright © 2026 **Nelson Secco Filho**.

Public access to this repository does not grant commercial-use rights.

See:

- [`LICENSE`](LICENSE)
- [`LICENSE-DOCS.md`](LICENSE-DOCS.md)
- [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md)

> This repository is source-available for noncommercial use. It should not be described as OSI Open Source because the public license restricts commercial use.

---

## Licenciamento

Este projeto utiliza um modelo de **licenciamento público para uso não comercial**.

- Framework, sistema de prompts, schemas, automações e materiais semelhantes a software: **PolyForm Noncommercial License 1.0.0**
- Documentação e conteúdo editorial: **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**
- Uso comercial: **reservado ao titular dos direitos e disponível apenas por meio de licença comercial separada e por escrito**

Copyright © 2026 **Nelson Secco Filho**.

O fato de o repositório ser público não concede direito de uso comercial.

Consulte:

- [`LICENSE`](LICENSE)
- [`LICENSE-DOCS.md`](LICENSE-DOCS.md)
- [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md)

> Este repositório disponibiliza o conteúdo-fonte para usos não comerciais. Ele não deve ser descrito como Open Source segundo a definição da OSI, pois a licença pública restringe uso comercial.

---

## Decision governance

Every significant decision made while evolving or applying this operating system should be documented.

Framework-level decisions are tracked through **Architecture Decision Records (ADRs)**:

- [`DECISION_LOG.md`](DECISION_LOG.md)
- [`docs/decisions/`](docs/decisions/)
- [`docs/decisions/ADR_TEMPLATE.md`](docs/decisions/ADR_TEMPLATE.md)

The rule is simple:

> **A significant decision is not complete until its rationale is documented.**

Accepted decisions are never silently rewritten. If new evidence changes a decision, a new record should supersede the previous one while preserving history.

Project/client decisions that contain confidential context should use the same model in a private/local decision log and must not be committed to the public repository.

---

## Repository structure

```text
ai-assisted-design-engineering-operating-system/
├── README.md
├── START_CHAT.md
├── PROMPT_OPERACIONAL_MASTER.md
├── PROJECT_CONTEXT_TEMPLATE.md
├── HANDOFF_TEMPLATE.md
├── WORKSTREAM_REGISTRY_TEMPLATE.md
├── SESSION_RECORD_TEMPLATE.md
├── RUNTIME_STATE_TEMPLATE.json
├── OPERATOR_PROFILE_TEMPLATE.md
├── DECISION_LOG.md
├── CHANGELOG.md
├── LICENSE
├── LICENSE-DOCS.md
├── COMMERCIAL-LICENSE.md
├── prompt-operacional.json
├── .gitignore
├── examples/
│   ├── PROJECT_CONTEXT.example.md
│   ├── HANDOFF.example.md
│   └── CHANGE_HISTORY.example.md
└── docs/
    ├── RATIONALE.md
    ├── PUBLICATION_CHECKLIST.md
    ├── CHANGE_RECORD_OWNERSHIP.md
    ├── PROJECT_RUNTIME.md
    └── decisions/
        ├── ADR_TEMPLATE.md
        └── ADR-0001 ... ADR-0014
```

Local runtime files are created from the templates and are not committed:

```text
PROJECT_CONTEXT.local.md
HANDOFF_CURRENT.local.md
```

---

## How to start a new AI session

Provide:

1. `START_CHAT.md`
2. `PROMPT_OPERACIONAL_MASTER.md`
3. `PROJECT_CONTEXT.local.md` if it exists
4. `HANDOFF_CURRENT.local.md` if it exists

If project context does not exist yet, the AI runs the First Run Onboarding.

If it exists, the AI validates the current tool state and continues from `NEXT ACTION`.

A returning session can begin with:

> continue

---

## Why Git?

The operating model benefits from the same properties that make source code maintainable:

- version history;
- diffs;
- rollback;
- traceability;
- explicit change records;
- canonical files;
- peer review.

Process instructions drift too. Versioning makes that drift visible.

---

## Consulting / product direction

This framework may be used as:

- an internal operating system for a designer or design team;
- a consulting accelerator for AI-assisted Product Design;
- a Design System governance layer for agentic workflows;
- a repeatable onboarding package for AI + Figma collaboration;
- a foundation for future automation or software.

The public repository documents the method. Client-specific context remains private.

---

## Suggested repository description

> Personal research and consulting framework for persistent AI-assisted Design Engineering workflows across Product Design, Design Systems, Figma, QA, and agentic tooling.

---

## Maturity

This is a living experiment, not a finished standard.

The framework should evolve as:

- AI agents become more capable;
- Figma and other design tools expose richer automation;
- MCP integrations change;
- Design Systems become more machine-readable;
- teams learn where AI autonomy helps and where human judgment must remain explicit.

---

# Português

## Por que este projeto existe?

A IA já consegue ajudar designers a inspecionar arquivos, compreender interfaces, gerar e modificar UI, trabalhar com Design Systems, revisar acessibilidade e automatizar partes da implementação.

O desafio deixa de ser apenas **o que a IA consegue fazer dentro de uma conversa**.

O problema operacional passa a ser:

> **Como preservar qualidade, contexto, evidências, governança e continuidade entre várias sessões de IA, ferramentas, arquivos, stakeholders e dias de trabalho?**

Sem um sistema operacional explícito, o humano vira a camada de memória.

Este repositório investiga um workflow reutilizável para resolver esse problema.

Ele é um **projeto pessoal de pesquisa e um framework de consultoria em evolução**. O framework público é intencionalmente neutro: nenhum cliente, empresa, stakeholder, Design System ou URL real de Figma deve ficar hardcoded nos arquivos canônicos.

---

## Dores do dia a dia

Um designer trabalhando intensamente com IA pode enfrentar repetidamente:

1. **Perda de contexto** — uma nova sessão não sabe o que a anterior validou.
2. **Repetição do método** — o humano precisa explicar novamente as mesmas regras operacionais.
3. **Design drift** — algo “parece melhor”, mas altera comportamento ou semântica já aprovados.
4. **Design System drift** — surgem duplicatas, alterações perigosas em tokens ou promoção prematura de padrões locais.
5. **Degradação das evidências** — referência antiga vence decisão nova ou hipótese vira “fato”.
6. **Estado da conversa ≠ estado da ferramenta** — o handoff diz uma coisa e o arquivo já mudou.
7. **Falha de ferramenta virando falha de workflow** — uma integração indisponível paralisa análises que ainda poderiam avançar.
8. **Carga cognitiva** — a IA devolve mais explicação do que o humano precisa para decidir e continuar.

O operating model reduz esses problemas com contexto explícito, provenance, classificação de risco, QA, handoff e um contrato de resposta curto:

`STATUS → EVIDENCE → ACTION → QA → NEXT`

---

## O que é “AI-Assisted Design Engineering”?

**Design Engineer** é uma direção útil para trabalhos que atravessam pensamento de produto, UI, Design Systems, prototipação e implementação.

Neste framework, **AI-Assisted Design Engineering** descreve a prática de inserir agentes de IA nesse loop operacional:

`compreender → inspecionar → comparar → decidir → mutar → validar → documentar → transferir contexto`

A IA não está apenas gerando UI. Ela participa de um processo governado, enquanto o humano continua responsável por julgamento de produto, intenção e responsabilidade final.

O título profissional exato é menos importante do que o operating model.

---

## Arquitetura

O framework separa três camadas:

### 1. Operating Model — estável

`PROMPT_OPERACIONAL_MASTER.md`

Define **como a IA deve trabalhar**.

### 2. Project Context — persistente, mas específico do projeto

Template público:

`PROJECT_CONTEXT_TEMPLATE.md`

Arquivo real/local:

`PROJECT_CONTEXT.local.md`

Define **onde e com quem estamos trabalhando**:

- organização;
- produto/projeto;
- stakeholder / decision-maker;
- Work Package / iniciativa;
- jornada / fluxo;
- nome e URL do Design System / UI Kit;
- nome e URL do arquivo principal de trabalho;
- governança;
- fontes de evidência.

### 3. Current Work State — volátil

Template público:

`HANDOFF_TEMPLATE.md`

Arquivo real/local:

`HANDOFF_CURRENT.local.md`

Define **o que estamos fazendo agora**.

---

## Project Runtime persistente

Para trabalhos de longa duração, o framework suporta um **Project Runtime**: uma memória operacional versionada e específica do projeto, independente da memória de uma conversa.

Ele preserva governança, decisões, Workstreams, handoffs, estado determinístico, identidades de operadores e Session Records.

Ele não substitui o estado real da ferramenta nem a evidência primária.

```text
Operating System = como trabalhamos
Project Runtime  = onde o estado operacional do projeto persiste
Ferramentas      = onde vive o artefato atual
Sessão de IA     = executor temporário
```

Veja [Project Runtime](docs/PROJECT_RUNTIME.md).

## Primeira execução

O framework começa em **modo genérico**.

Ele não deve presumir empresa, stakeholder, Design System, projeto ou arquivo.

Quando ainda não existir contexto de projeto, a IA solicita somente os dados mínimos e explica brevemente por que eles importam.

Campos iniciais recomendados:

| Campo | Por que importa | Obrigatório inicialmente? |
|---|---|---:|
| Organização / cliente | Identidade e separação de contextos | Não |
| Produto / projeto | Define o domínio do trabalho | Sim |
| Stakeholder / decision-maker principal | Ajuda a classificar autoridade de aprovação | Sim |
| Work Package / iniciativa | Limita o escopo quando aplicável | Não |
| Jornada / fluxo | Define a área atual do produto | Sim |
| Nome do Design System / UI Kit | Identifica a fonte canônica de design | Condicional |
| URL do Design System / UI Kit | Permite inspeção direta | Condicional |
| Nome do arquivo de trabalho | Identifica o arquivo ativo | Sim antes da execução |
| URL do arquivo de trabalho | Permite inspeção direta | Sim antes da execução |

Informações adicionais são pedidas **just in time**, e não como um formulário gigante.

Exemplos:

- referência aprovada / source of truth;
- Local Components;
- documentação de governança;
- gravações / transcrições;
- tickets ou requisitos;
- restrições de implementação.

> **O contexto deve ser coletado quando se torna necessário, e não todo de uma vez.**

---

## Modelo de privacidade

O repositório público contém **o método**, não o contexto real de clientes ou projetos.

Estes arquivos ficam ignorados pelo Git:

```text
PROJECT_CONTEXT.local.md
HANDOFF_CURRENT.local.md
*.private.md
.env
```

Nunca coloque diretamente no framework canônico:

- nome real de cliente ou empresa;
- nome real de stakeholder;
- URLs internas do Figma;
- Design Systems privados;
- credenciais;
- evidências proprietárias.

Esses dados pertencem aos arquivos locais de runtime.

---

## Como iniciar uma nova sessão

Forneça:

1. `START_CHAT.md`
2. `PROMPT_OPERACIONAL_MASTER.md`
3. `PROJECT_CONTEXT.local.md`, se existir
4. `HANDOFF_CURRENT.local.md`, se existir

Se ainda não houver Project Context, a IA executa o First Run Onboarding.

Se já houver, ela valida o estado atual das ferramentas e continua a partir de `NEXT ACTION`.

Uma sessão recorrente pode começar apenas com:

> seguir

---

## Direção de consultoria / produto

Este framework pode evoluir para:

- operating system interno para designers ou times de design;
- acelerador de consultoria para Product Design assistido por IA;
- camada de governança de Design Systems em workflows agênticos;
- onboarding reutilizável para colaboração IA + Figma;
- base para automações ou software futuro.

O repositório público documenta o método. Contextos específicos de clientes permanecem privados.

---

## Descrição sugerida para o repositório

> Personal research and consulting framework for persistent AI-assisted Design Engineering workflows across Product Design, Design Systems, Figma, QA, and agentic tooling.

---

## Maturidade

Este é um experimento vivo, não um padrão finalizado.

O framework deve evoluir conforme agentes, ferramentas, MCP e Design Systems evoluírem.

## Mutation-owned Change History / Histórico no owner

**THE FILE / ARTIFACT THAT OWNS THE MUTATION OWNS THE CHANGE RECORD**

Significant mutations have persistent records at each actually changed owner. Read-only dependencies and cited consumer evidence do not gain change records. Shared libraries are not central consumer logs. Register each history location and namespace in project context; establish missing owner history before finalization. Linked multi-owner records and append-only historical corrections preserve traceability. Handoff and chat memory do not replace persistent records.

Mudanças significativas são registradas em cada artefato realmente mutado. Dependências inspecionadas e evidências de consumers não geram records sem mutação. Registre localização e namespace por owner no contexto; resolva history ausente antes de FINAL. Correções históricas preservam o original como evidência archived/pointer e criam cópia canônica vinculada no owner correto.

See [guide](docs/CHANGE_RECORD_OWNERSHIP.md), [ADR-0014](docs/decisions/ADR-0014-mutation-owned-change-records.md) and [generic scenarios](examples/CHANGE_HISTORY.example.md). Run `python scripts/validate_framework.py` plus [publication QA](docs/PUBLICATION_CHECKLIST.md). There is no dependency installation step. Startup order remains Master → Project Context → Handoff → relevant owner governance/records → current inspection → safe next action.
