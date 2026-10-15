# Design foundation provenance and whole-screen QA

**Ownership:** SHARED_CONTRACT. **Maturity:** unreleased generic candidate derived from an adopted project gate; whole-file effectiveness has not been demonstrated. Apply within existing authorization, risk and design-system change control. This is an additive QA clarification, not a new task-state schema.

## Inspect current foundations before composing

Inspect the current canonical Design System and published component inventory. Prefer native linked instances. Verify the relevant published typography, semantic color variables, spacing, padding, radius, borders and token-defined dimensions.

Custom content inside a linked component slot needs its own provenance checks. Use published text styles and semantic bindings, not visually similar manual values. Where binding is unsupported, disclose the constraint and preserve the established equivalent only through the existing exception route. Distinguish dynamic constraints-driven positioning from authored token spacing.

Inspect actual component keys, variants, properties, style IDs and bound variables together with the rendered result. If a foundation is missing, conflicting or inaccessible, report the specific evidence, alternatives and risk. Do not invent shared tokens or publish a foundation without authority.

## Check the whole affected screen before review

Human review does not replace baseline conformance checks. Review the complete affected visible hierarchy: overlays and backdrops, shell and navigation, surfaces, content, dialog slots, controls, footer actions, icons and state-dependent layers. Compare canonical examples for properties, token/style provenance, opacity, dimensions, stacking, layout, effects, visibility and behavior.

A passing dialog subtree does not prove its surrounding screen conforms. A small sample cannot establish whole-file compliance. Inspect all relevant states and affected consumers before making that broader claim.

Correct an obvious local deviation when the existing canonical pattern and prior authorization cover it. Missing or conflicting shared patterns, API changes and business-semantic changes follow their existing decision gates. Tool failure does not authorize a workaround that circumvents a restriction.

## Record evidence and limits

Record per-screen criteria and results, exact private artifact locators in the private owner record, structural readback, full-screen visual evidence and relevant component/foundation provenance. Inspect expanded native annotations and labels where they affect the review surface; bounding boxes alone are insufficient.

Use the existing project QA vocabulary. Unchecked scenes stay pending; passing a layout check does not validate functional permissions, runtime behavior or stakeholder acceptance. Track actual failures and approved exceptions. Do not label a complete journey ready for human review when an essential affected scene remains unverified.

Actual changes use owner Change History and the existing Git/handoff conventions. This contract does not require a second QA tracker, authorize library publication, or claim the original adopter's complete screen set passed.
