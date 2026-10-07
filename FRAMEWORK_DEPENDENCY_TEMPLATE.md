# FRAMEWORK DEPENDENCY — TEMPLATE

**Canonical framework repository:** <public framework URL>  
**Stable immutable framework pin:** <full commit SHA>  
**Framework version:** <version>  
**Vendored Master path:** <path>  
**Runtime version:** <independent project-runtime version>  
**Framework candidate:** <PR / branch / commit / none>

Vendor the generic Master from the declared stable pin without editing its generic rules. Verify content parity and resolve all companion references. Project-specific configuration belongs in context/governance/manifest, not in the Master.

A newer candidate is not the stable pin. Record the candidate, its validation gates and relevant project overrides until promotion. After the generic change merges, update the private dependency pin and vendored companions in a governed PR and rerun static QA.

Runtime version, framework version and schema versions are independent; compare each against its own source rather than forcing identical numbers.
