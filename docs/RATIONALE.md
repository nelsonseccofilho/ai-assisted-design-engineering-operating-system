# RATIONALE
## Why this operating system exists

This document explains the reasoning behind the **AI-Assisted Design Engineering Operating System**.

It is not an operational prompt.

It is the design rationale for the framework itself: the problem it addresses, the assumptions behind its architecture, the daily pains it is intended to reduce, and the way humans and AI are expected to collaborate.

---

# 1. The problem

AI can already help designers:

- inspect interfaces;
- analyze UX;
- generate UI;
- manipulate design tools;
- review components;
- compare implementations;
- work with Design Systems;
- reason about accessibility;
- document decisions;
- assist implementation.

The difficult part is no longer only:

> “Can the AI perform this task?”

A more important question is:

> **Can the human + AI workflow remain reliable over time?**

Real design work is persistent.

It may last days, weeks, or months and involve:

- multiple conversations;
- multiple design files;
- different stakeholders;
- changing requirements;
- several evidence sources;
- Design System dependencies;
- implementation constraints;
- review cycles;
- decisions that can later be superseded.

Most AI conversations, however, are session-oriented.

That creates a structural mismatch:

```text
long-running product work
        versus
session-based AI context
```

Without an explicit operating model, the human has to bridge that gap manually.

---

# 2. The core pain

The central problem can be summarized as:

> **Without an explicit operating system, the human becomes the memory layer.**

The designer ends up remembering:

- what was already decided;
- which evidence is authoritative;
- what the AI may or may not change;
- what was approved;
- what still needs QA;
- which component is canonical;
- what belongs locally;
- why something was intentionally left untouched;
- where the work stopped;
- what the next session must do.

This is cognitively expensive.

It also creates risk.

The more complex the project becomes, the more likely it is that:

- context is lost;
- old decisions return;
- assumptions become facts;
- design drifts;
- systems drift;
- work is duplicated;
- QA becomes inconsistent;
- important constraints disappear between sessions.

---

# 3. Why a prompt alone is not enough

A long prompt can define behavior, but it does not solve every continuity problem.

A single prompt tends to mix three different types of information:

## Stable rules

Examples:

- how evidence should be prioritized;
- how to distinguish UI from business rules;
- when Design System components may be created;
- what QA means;
- how the AI should communicate.

These rules change slowly.

## Project context

Examples:

- project name;
- stakeholder;
- Design System;
- work file;
- governance location;
- source-of-truth references.

These change from project to project.

## Current work state

Examples:

- current task;
- what was already changed;
- pending QA;
- unresolved assumptions;
- next action.

These can change several times per day.

Putting all three into one prompt makes the system:

- harder to maintain;
- harder to reuse;
- easier to contaminate with stale information;
- more cognitively expensive;
- less portable between projects.

The framework therefore separates them.

---

# 4. The architecture

The operating system uses three main layers.

## 4.1 Operating Model

Defined by:

`PROMPT_OPERACIONAL_MASTER.md`

It answers:

> **How should the AI work?**

It contains:

- roles;
- evidence hierarchy;
- governance;
- execution rules;
- risk classification;
- preflight;
- postflight;
- QA;
- documentation;
- handoff rules;
- completion criteria.

This layer should remain project-independent.

---

## 4.2 Project Context

Created from:

`PROJECT_CONTEXT_TEMPLATE.md`

It answers:

> **Where are we working, with whom, and inside which design environment?**

It may contain:

- Organization / Client;
- Product / Project;
- Primary stakeholder;
- Work Package / Initiative;
- Journey / Flow;
- Design System / UI Kit;
- work file;
- approved reference;
- Governance location;
- evidence sources.

This layer is project-specific.

For public repositories or shared frameworks, real context should remain local and private.

---

## 4.3 Current Handoff

Created from:

`HANDOFF_TEMPLATE.md`

It answers:

> **What are we doing right now, what happened, and what happens next?**

It contains:

- current objective;
- evidence;
- completed work;
- decisions;
- QA status;
- open assumptions;
- constraints;
- pending work;
- last action;
- exact next action.

This layer is intentionally short-lived.

---

# 5. Why context is collected progressively

The framework does not ask for every possible field at startup.

Doing so would create a long onboarding form before useful work begins.

Instead, it uses:

> **Just-in-time context collection**

The first execution should collect only what is necessary to identify the work.

Typical initial context:

- Product / Project;
- Primary stakeholder;
- Journey / Flow;
- Design System / UI Kit;
- work file.

Additional information is requested only when it becomes operationally relevant.

Examples:

- approved reference when parity work begins;
- Governance location before high-impact mutations;
- evidence sources when conflicting requirements appear;
- consumer impact when a shared component changes.

This reduces human cognitive load.

---

# 6. Why evidence needs a hierarchy

AI systems are good at producing plausible interpretations.

Product work requires more than plausibility.

A designer may have:

- stakeholder approval;
- video recordings;
- current product behavior;
- Design System rules;
- historical components;
- external UX guidance.

These sources do not have equal authority.

Without an explicit hierarchy, the AI might replace a product-specific decision with a generic “best practice”.

The operating system therefore requires:

> **Evidence before preference**

And distinguishes:

- FACT;
- INFERENCE;
- ASSUMPTION.

It also tracks whether a source is:

- CANONICAL;
- HISTORICAL EVIDENCE;
- SUPERSEDED.

This prevents old or inferred information from silently becoming authoritative.

---

# 7. Why the current tool state matters

A handoff is useful, but it is still a snapshot.

The actual design file may change after the handoff was written.

Therefore:

> **Current inspectable tool state takes precedence over stale conversational state.**

This does not mean ignoring the handoff.

It means reconciling:

```text
handoff says X
tool currently shows Y
        ↓
investigate the difference
        ↓
update current state
```

This reduces the risk of continuing work based on outdated context.

---

# 8. Why Design System governance is central

AI-assisted design becomes more powerful when the AI can mutate real systems.

That also increases risk.

A seemingly small change can affect:

- many consumers;
- component APIs;
- tokens;
- variants;
- accessibility;
- visual consistency;
- implementation contracts.

The framework therefore separates:

```text
local solution
        versus
canonical system change
```

And asks:

- is this pattern truly systemic?
- does it recur?
- can it exist outside this journey?
- what consumers will be affected?
- is a global mutation necessary?

This protects the Design System from becoming a collection of project-specific exceptions.

---

# 9. Why “parity before evolution”

AI tends to optimize.

That is useful during ideation.

It can be dangerous during reconstruction.

When reproducing an approved interface, premature optimization can accidentally remove:

- business information;
- states;
- hierarchy;
- semantic distinctions;
- interactions;
- approved behaviors.

Therefore:

> **Reconstruct first. Evolve second.**

Or:

> **Parity before UX evolution.**

Improvement remains encouraged, but it becomes a separate, explicit phase.

---

# 10. Why QA is broader than visual inspection

A screen can look correct and still be wrong.

The operating system treats QA as multiple layers:

## Visual QA

- hierarchy;
- spacing;
- alignment;
- iconography;
- semantic color;
- rendering.

## Structural QA

- component ownership;
- instances;
- properties;
- Auto Layout;
- hidden layers;
- empty residues;
- broken references.

## Functional / semantic QA

- states;
- actions;
- information;
- business rules;
- labels;
- transitions.

## Documentation QA

- decision recorded;
- evidence recorded;
- consumer impact recorded;
- publication notes prepared when needed.

“Looks correct” is only one part of “is correct.”

---

# 11. Why the AI should be autonomous — but bounded

Requiring approval for every small action makes AI collaboration slow and exhausting.

Allowing unrestricted mutation creates risk.

The framework therefore uses bounded autonomy.

## Low-risk work

The AI may proceed autonomously when:

- evidence is clear;
- scope is local;
- impact is small;
- rollback is easy.

## High-impact work

The AI should add safeguards when:

- changing global tokens;
- changing shared components;
- altering component APIs;
- deprecating assets;
- performing migrations;
- affecting many consumers.

The principle is:

> **Autonomy should scale with confidence and reversibility.**

---

# 12. Why tool failure should not stop reasoning

A temporary integration failure does not make all work impossible.

If the AI cannot safely mutate, it may still:

- inspect available evidence;
- compare;
- map dependencies;
- identify inconsistencies;
- prepare QA;
- document uncertainty;
- propose the next safe action.

The framework therefore distinguishes:

> **cannot mutate safely yet**

from:

> **cannot make progress**

This makes the workflow more resilient.

---

# 13. Why human-first communication matters

AI has low cost for generating text.

Humans have limited attention.

A system that produces unnecessarily long explanations may technically be complete while making the actual work harder.

The operating system therefore prefers a compact operational contract:

```text
STATUS
EVIDENCE
ACTION
QA
NEXT
```

This helps the human answer quickly:

- Where are we?
- Why?
- What changed?
- Is it valid?
- What happens now?

The goal is not maximum verbosity.

The goal is **operational clarity**.

---

# 14. What this framework is intended to improve

The framework aims to reduce:

- context reconstruction;
- repetitive prompting;
- design drift;
- Design System drift;
- accidental scope expansion;
- duplicate components;
- loss of evidence;
- stale decisions;
- inconsistent QA;
- human memory dependency;
- cognitive overhead between sessions.

And improve:

- continuity;
- traceability;
- autonomy;
- safety;
- reuse;
- governance;
- clarity;
- transferability between projects;
- collaboration between human and AI.

---

# 15. Typical usage flow

```text
clone / open framework
        ↓
START_CHAT
        ↓
no project context?
        ↓
collect minimum context
        ↓
PROJECT_CONTEXT.local.md
        ↓
inspect current design environment
        ↓
preflight
        ↓
execute bounded changes
        ↓
QA
        ↓
document decisions
        ↓
continue work
        ↓
session approaching limit?
        ↓
generate HANDOFF_CURRENT.local.md
        ↓
new AI session
        ↓
reconcile handoff with current tool state
        ↓
continue from NEXT ACTION
```

---

# 16. What this is not

This framework is not:

- a substitute for Product Design judgment;
- a substitute for stakeholder decisions;
- a universal UX rulebook;
- a fully autonomous product designer;
- a Design System by itself;
- a Figma-only methodology;
- a requirement to use one specific AI model.

It is an operating layer for coordinating:

> **human judgment + project evidence + design tooling + AI execution**

---

# 17. Why this may become a consulting product

Many teams adopting AI in design focus first on tool access:

- connect Figma;
- generate UI;
- automate components;
- use coding agents.

Tool access alone does not create a reliable operating model.

A consulting engagement around this framework could help a team define:

- AI operating rules;
- context architecture;
- evidence hierarchy;
- Design System governance;
- autonomy boundaries;
- QA protocol;
- handoff strategy;
- project templates;
- private/public context separation;
- agent onboarding;
- reusable workflows.

The consulting value is not simply:

> “use AI in design.”

It is closer to:

> **design and operationalize a reliable human + AI design workflow for real product environments.**

---

# 18. Product hypothesis

A longer-term hypothesis behind this research is that this workflow could evolve from documentation into a product.

Possible forms include:

- a reusable operating framework;
- a CLI/bootstrap tool;
- an AI workspace initializer;
- a Figma/agent governance layer;
- an MCP workflow orchestrator;
- a project-context manager;
- a handoff generator;
- a Design System agent policy layer;
- a consulting accelerator.

This is a hypothesis, not a fixed product direction.

The documentation exists partly to make the learning explicit enough to evaluate that hypothesis.

---

# 19. Success criteria

This operating system is useful if it makes the following easier:

### For the designer

- start a new AI session without reconstructing the project;
- trust that known constraints will be respected;
- understand what the AI changed;
- identify unresolved uncertainty;
- review work with less cognitive load.

### For the AI

- understand what is canonical;
- distinguish facts from assumptions;
- know what it may change;
- know what it must validate;
- recover current context reliably.

### For the organization

- make AI-assisted design work more traceable;
- preserve Design System integrity;
- reduce accidental drift;
- create reusable operating knowledge.

---

# 20. Core idea

The framework can be reduced to one principle:

> **AI should not depend on the human to continuously reconstruct the operating context required to work safely.**

Instead, that context should be:

- explicit;
- structured;
- versionable;
- inspectable;
- transferable;
- minimal enough to remain usable.

That is the rationale behind the AI-Assisted Design Engineering Operating System.


---

# 21. Why decisions need permanent records

A handoff answers what is happening now.

A changelog answers what changed between versions.

Neither fully answers:

> **Why did we choose this direction?**

Without a permanent decision record, a later session may see the current state but lose the reasoning that produced it.

The framework therefore uses decision records for significant choices.

A good decision record preserves:

- the problem that existed;
- the evidence available at the time;
- the selected decision;
- why it was selected;
- alternatives considered;
- impact and trade-offs;
- conditions that may justify revisiting it.

This prevents “organizational amnesia” across human and AI sessions.

The goal is not to document every micro-action.

The goal is to document every decision whose loss would make future work harder to understand, audit, reverse, or evolve.

# 22. Why mutation owners retain history

Centralizing consumer changes in a shared library confuses dependency authority with mutation ownership. Owner-scoped history preserves where the actual mutation occurred while linked records preserve coordination. Evidence-only references remain useful without claiming a mutation. ADR-0014 adds this rule without changing the Operating Model / Project Context / Handoff architecture. Decisions explain rationale; Change History documents mutation; handoff and chat memory provide continuity. See [ownership guide](CHANGE_RECORD_OWNERSHIP.md).
