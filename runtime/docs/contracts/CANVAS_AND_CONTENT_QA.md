# Canvas integrity and content-stress QA

**Ownership:** SHARED_CONTRACT. **Maturity:** proposed checks plus optional layout pilot. No private dimensions or spacing values are universal standards.

## Containment and dependency checks
Inspect the actual owning page/section, parentage, IDs, nearest neighbors and preserved landmarks before mutation. A screen placed correctly in absolute coordinates can still be an orphan outside its owning section. Owner history belongs inside its registered history surface.

After additions, deletion, resize or movement, verify containment, sibling collisions, labels, annotations, connectors and dependent regions. Model a dependent region relative to its source bounds and a locally justified clearance; recompute both in the same authorized change. The relationship is procedural unless the tool actually implements it.

Native editor labels and expanded annotations may occupy space outside node bounds or be absent from API screenshots. Keep structural geometry QA separate from native visual inspection and practical zoom/readability. Record the latter NOT RUN when unavailable. Do not fabricate visual PASS from zero rectangular intersections.

Preserve approved content and intentional deletions. Missing historical nodes require current-state reconciliation, not automatic recreation or attribution of who removed them. Distinguish evidence of a deletion from permission to restore it.

## Responsive content and scroll
Separate full-content authoring, static viewport examples, interactive prototype behavior and application runtime. A clipped still image, configured overflow property or visible scrollbar drawing does not prove reachable content.

Use representative short/long content, empty/single/multiple entries, long unbroken identifiers, unusual characters and large-text/zoom conditions where applicable. Check header/footer reachability, focus movement, sticky/fixed controls, nested scroll regions, truncation meaning and hidden controls. Preserve exact evidence IDs; do not hide content to make containment pass.

If the selected scope is static presentation, label interactive/runtime checks NOT RUN or explicitly out of that scope. Do not retrofit an interaction merely to satisfy a test for a different deliverable. Required runtime/security acceptance remains separate.

Repeated scene-specific repairs should trigger root-cause inspection of the source component and all actually affected consumers. Recheck a bounded sample as a sample; counts alone cannot certify an entire file.
