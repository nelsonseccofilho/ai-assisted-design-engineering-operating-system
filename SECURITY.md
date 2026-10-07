# Framework security and privacy

This public repository contains generic method, templates, validators and fictional examples.

## Public boundary

Never publish client/stakeholder identities, populated operator profiles, real sessions/reports, private runtime repository URLs, artifact file keys/node IDs/change IDs, proprietary evidence, credentials, tokens or signing keys.

Populated operators/, sessions/, workstreams/ and reports/ belong in a separate governed private runtime. Ignored paths are defense in depth; inspect the actual staged diff and scan before publication.

## Private runtime boundary

A project may intentionally version approved operational context in a private repository. Keep repository visibility and access governed. Private visibility does not permit authentication secrets, unapproved full transcripts, heavyweight raw meeting recordings or raw exports.

## Upstreaming

Derive organization-agnostic behavior from pilot evidence. Replace project values with placeholders and configurable policies before upstreaming. Scan both the diff and candidate tree. If sensitive material was exposed, stop further publication, inform the owner through an authorized channel and arrange credential revocation when relevant; history preservation does not justify retaining exposed credentials.
