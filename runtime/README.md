# Project Runtime package

This directory is the **canonical deployable Project Runtime layout**.

The same relative paths are used in every adopting runtime.

The public repository contains generic/configurable seeds. A private project repository contains the same structure populated with real operators, sessions, workstreams, reports, evidence and project decisions.

Compare repositories at `runtime/`, not at repository root.

## Starting from a brand-new chat

A new chat does **not** mean "continue the previous chat".

The first step is to declare the startup intent.

### Continue existing work

```text
Load the Project Runtime from main using runtime/00_START_CHAT.md.
Intent: CONTINUE_WORKSTREAM.
Continue <WORKSTREAM-ID or described work>.
Report the recovered state before mutation.
```

### Start a new task / journey / flow in the same project

```text
Load the Project Runtime from main using runtime/00_START_CHAT.md.
Intent: START_NEW_WORKSTREAM.
New work: <describe the task, journey, flow or objective>.
Do not continue an existing Workstream by default.
Check mutation-scope overlap, create a new Workstream if appropriate, and report the initialized state before mutation.
```

### Start a completely new project/client

```text
Use the generic Operating System runtime package.
Intent: START_NEW_PROJECT.
Create a separate private Project Runtime for <project>.
Do not reuse populated context, sessions, evidence, reports, Decisions or Workstreams from another project.
Collect only the minimum project context needed to initialize safely.
```

## Base operating rule

Every mode still applies the same base contract:

`load runtime → resolve identity/access/intent → inspect evidence and current artifact state → resolve ownership/scope → act → validate → persist → hand off`
