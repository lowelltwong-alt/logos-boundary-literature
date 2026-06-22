# Schemas

These JSON Schemas are planning scaffolds for future metadata and scoped claim records.

They do not authorize source ingestion and do not define canonical Scripture records.

- `work.schema.json`: boundary work metadata.
- `source_status.schema.json`: acquisition/license/source-review status.
- `trust_profile.schema.json`: trust-level governance profile.
- `boundary_claim.schema.json`: scoped noncanonical/reception/background claims.
- `reliability_evidence_database_plan.md`: metadata-only plan for Bible reliability,
  provenance, manuscript-evidence, reception, and apologetics research.
- `reliability_evidence_source_spine.md`: source-spine scaffold separating confirmed
  source metadata from candidate apologetic or historical claims.
- `reliability_evidence_intake_queue.md`: pre-evidence intake queue plan for
  source candidates, repo routing, and review gates.
- `reliability_evidence_method_profiles.md`: method-profile plan for dating,
  source-language, textual-variant, patristic-citation, and discovery-context review.
- `reliability_evidence.sqlite.schema.sql`: SQLite scaffold for boundary-owned and
  derived evidence tables. It does not define canonical Scripture tables or store source text.
