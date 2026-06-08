# Rules Registry

These rules are proposed governance rules for the scaffold. They do not authorize source ingestion.

| Rule | Importance | Context | Failure prevented | Applies when | Override policy | Examples |
| --- | --- | --- | --- | --- | --- | --- |
| `BOUNDARY-001 - Boundary Literature Is Not Canonical Scripture` | P0 | Boundary works can be useful without being Scripture. | Treating boundary texts as Word of God. | Any work/claim enters this repo. | Human canon/tradition review only. | 1 Enoch as background, not default Scripture. |
| `BOUNDARY-002 - Trust Level Must Be Explicit` | P0 | Works vary from high-trust background to known fake. | Flattening all noncanonical works into one bucket. | Creating work or claim records. | Human trust review. | Josephus vs Gospel of Judas vs modern fake gospel. |
| `BOUNDARY-003 - Canon Status Is Tradition-Scoped` | P0 | Canon status differs by tradition. | Overwriting tradition-specific authority. | Discussing deuterocanon/apocrypha/canon status. | Human canon review. | Tobit, Sirach, 1-2 Maccabees. |
| `BOUNDARY-004 - Known Forgeries Are Quarantined` | P0 | Known fakes can contaminate retrieval. | Fake works used as trusted background. | Work has reviewed forgery/fake status. | Human review can allow refutation-only use. | Modern fake gospels. |
| `BOUNDARY-005 - High-Trust Background Is Still Not Word of God` | P0 | Background value is not canonical authority. | Treating 1 Enoch/Jubilees as Scripture in default scope. | High-value noncanonical background is cited. | Tradition/profile review only. | 1 Enoch and Jude reception. |
| `BOUNDARY-006 - Commentary/Reception Claims Are Not Canonical Claims` | P0 | Reception claims can influence interpretation. | Commentary mutates Scripture truth. | Commentary or reception records are created. | Explicit tradition/profile review. | Patristic interpretation. |
| `BOUNDARY-007 - No Generic Related-To Links` | P1 | Generic links hide authority and direction. | Cross-repo contamination. | Creating relationships. | Schema review only. | Use `boundary_text_references_scripture`. |
| `BOUNDARY-008 - No Text Ingestion Without Source Review` | P0 | Source texts carry license and contamination risk. | Importing unsafe or copyrighted corpora. | Any source intake occurs. | Human source/license review. | DSS translations, modern editions. |
| `BOUNDARY-009 - No Cross-Repo Contamination` | P0 | Repos have separate authority domains. | Boundary claims become canonical Scripture claims. | Cross-repo references are created. | Human contract review. | Scripture repo points here as background only. |
| `BOUNDARY-010 - Claims Need Provenance` | P0 | Claims without source are unsafe. | Untraceable theology or attribution claims. | Creating boundary claims. | No override except quarantine triage. | Claim needs work/source/evidence refs. |
| `BOUNDARY-011 - Boundary Repo Is Never Equal Scripture Authority` | P0 | Boundary literature can support comparison, reception, refutation, and background. | Boundary material overrides or equals canonical Scripture authority. | Any cross-repo claim, retrieval, or interpretation uses boundary material. | Governance + human authority review only; default is fail closed. | Stop if boundary material appears required to modify canonical Scripture outputs. |
