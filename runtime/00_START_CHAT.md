# Runtime startup

Read runtime-manifest.json from the canonical main ref first. Classify access as READ_WRITE, READ_ONLY or UNAVAILABLE. Load its bootstrap_files in order, skipping this entry point when encountered. Load selected Workstream HANDOFF/state and relevant Session Records. Resolve Human operator, Operator alias and Chat label separately; reconcile current artifact state before mutation. See the Master for ownership, context-limit and session-closure rules.

Resolve report commands, languages and requirement from the manifest. DRAFT never advances the cursor; confirmed SENT advances to frozen interval_end. WAIVED does not advance it. Never infer that a repository checkpoint closed the chat or validated live gates.

Before updating shared files, run scripts/runtime_sync.py against an independently fetched immutable framework checkout. Configured files require review; never overwrite project data from templates. Keep stable and candidate pins distinct.
