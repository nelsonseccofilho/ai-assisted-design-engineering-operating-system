# Fictional native annotation and layout observations — 2026-10-15

**Targets:** METH-023 and METH-024. **Released architecture:** 3.6.0.
**Closure:** COMPLETED_WITH_CAVEATS for one authorized fictional Design-file unit only, under [GOV-VAL-001](../runtime/docs/contracts/VALIDATION_AND_CLOSURE.md). This is an evidence assessment, not a runtime state, general pilot acceptance or release.

## Question and acceptance fixed before execution

Can a local fictional component/instance fixture demonstrate native annotation scope, observable editor occupancy/readability and dependent reflow when a separate contextual canvas panel grows?

The local plan fixed eight mandatory cases before the file was created: identity/containment, a real native annotation, editor visualization, dependent layout, short/long text, local component update, scope isolation and final readback. The editor case required current native captures with display state and zoom recorded; exported nodes and rectangular geometry could not substitute. The fixture explicitly excluded existing design files, private runtime changes, external library publication and consumer synchronization.

The eight-case unit was assessed, with the native editor case completed after earlier access failures. Previous still-valid API/canvas observations were reused, not rerun as new experiments. Closure is limited to these criteria and the display states actually observed below; it does not satisfy the broader pilot's individual collapsed/expanded or post-library-sync criteria.

## Environment and provenance

One new, wholly invented Figma Design file contained one local main component, two instances, a native annotation on only the narrower instance, a separate contextual auto-layout panel per screen, a dependent region and an unrelated control. File discovery preceded creation; no existing/private library component or design artifact was imported. Local primitive/semantic variables and text styles supplied the fixture foundations. Operational identifiers, account/team information and source captures remain restricted.

The authoring AI executed and assessed the fixture through the native editor in authenticated Chrome and the Figma API. This is one synthetic case, not independent human review, a representative sample or an external replication. The maintainer supplied access; that does not establish human comprehension or product acceptance.

## Observed results

| Case | Observation and evidence scope |
|---|---|
| N1 — Identity and containment | API tree/geometry identified the local section, main component, both instances and dependent regions. The earlier final tree had no containment violations. The later history extension remained contained in its enlarged section. |
| N2 — Native annotation | API readback identified a real annotation, the file's existing Content category and the intended instance. The other instance remained without an annotation. The canvas panel was a separate frame, not a simulated native annotation. |
| N3 — Editor visualization | Current editor captures recorded annotation visible, hidden and restored at 75%. The category and full note were readable; hiding removed the overlay, and restoring brought back the same note. Occupancy and label limitations are retained below. This was the native Annotations display control, not an individual note collapsed into an icon. |
| N4 — Dependent reflow | With fixture screen widths of 360 and 720 px, longer panel content grew the panels by 198 and 88 px respectively. Their dependent regions moved by the corresponding distance and preserved an 8 px gap. These are fixture measurements, not universal spacing or evidence that a native overlay moves nodes. |
| N5 — Content stress | Short/long content, including a long unbroken invented sample, was visible in rendered canvas captures at both declared widths without observed clipping or collision. This is static presentation evidence, not application responsiveness, scroll reachability or accessibility acceptance. |
| N6 — Local component update | Changing the main component's top padding from 16 to 24 px increased both instance heights by 8 px while retaining source identity and instance-specific text. No published library or cross-file synchronization was exercised. |
| N7 — Scope isolation | Final readback retained the note only on its target, preserved both local component links/overrides and left the unrelated control unchanged in the checked geometry/content/annotation scope. |
| N8 — Final readback | The lab's owner history retained earlier entries and appended the actual native observation. Its section was extended only to contain the growing history. API readback and a current editor overview confirmed that final composition; the overview's small text was not used as readability evidence. |

These are eight scoped checks of one fixture, not eight participants or independent trials. Earlier measurements remain attributed to their original execution; the UI resumption supplied the previously missing native-display observation.

## Native occupancy and legibility caveats

At 75%, the annotation overlay extended left of its target and obscured part of the neighboring main component. The note and target titles remained readable in the inspected framing. Some auxiliary editor-generated labels had weak contrast against the light canvas. At 100% with full sidebars, the initial framing left part of the annotation behind a sidebar. The panels were temporarily minimized to inspect the note; the normal panels and Design mode were restored afterward.

The closed observation used the editor's Annotations visibility option: the UI reported annotations hidden and removed the note from view. Re-enabling it reported annotations visible and restored the same note. Closed/restored captures used the same 75% scale and framing. A subsequent API readback retained the annotation content/category/target and local component links. No individual collapsed-icon behavior, automatic clearance, viewport-independent legibility or absence of all overlay collisions is established.

The final 28% overview checked composition and containment only. API/canvas capture, native UI visibility, individual collapse behavior and human usability remain different evidence. No contrast-conformance claim or new universal margin follows from this observation. The overlap and weak labels were recorded rather than removed to manufacture a cleaner result.

## Access failures and evidence retention

Earlier browser attempts reached an unauthenticated editor; a later attempt lost Chrome control before authenticated native inspection. The native editor case remained NOT RUN during those attempts. They were access/setup limitations, not a failed annotation assertion or passing visual evidence. After reconnection and maintainer login, actual editor inspection became possible. The fixture, acceptance criteria and earlier API/canvas outcomes were retained.

Restricted local evidence includes the pre-execution plan, initial/reflow/component/final API observations, canvas renders, native visible/hidden/restored captures and the final owner-history readback. The old failed-access and partial-result records remain historical, with the completed result explicitly superseding their pending checkpoint. Raw screenshots expose operational UI details and are deliberately excluded from this public report; public review can assess the sanitized account but cannot independently inspect those restricted captures here.

## Disposition and next decision

METH-023 remains OPTIONAL_PILOT / NARROWLY_VERIFIED; METH-024 remains OPTIONAL_PILOT / PILOT_PENDING. Their catalog validation scopes now include this bounded native evidence without changing maturity, disposition, release status or existing ADR status. No runtime contract, bootstrap, schema/state, dependency pin, license or private adopter was changed by this documentation delivery.

The [next-cycle plan](PILOT_VALIDATION_NEXT_CYCLE.md) retains independent human reading, individual collapsed/expanded occupancy and post-publication cross-file consumer adoption as separate gaps. A broader native or library trial needs its own concrete decision, authorized environment and predeclared acceptance; do not rerun this unchanged fixture simply because the work resumes. The [human packet](HUMAN_HANDOFF_TRIAL.md) remains prepared with human execution NOT RUN, and the delivery-efficiency comparison remains deferred.

For this public candidate, the six existing local workflow steps, privacy/protected-file review and immutable changed-file readback remain required. Their actual results belong in its PR record. [Hosted CI](HOSTED_CI_STATUS.md) remains separately suspended; local QA is not hosted PASS or permission for merge, release or pilot promotion. Existing [ADR-0025](decisions/ADR-0025-pilot-maturity-and-promotion.md) and [ADR-0029](decisions/ADR-0029-risk-proportionate-validation.md) govern this bounded evidence update; no new policy or acceptance decision is introduced.
