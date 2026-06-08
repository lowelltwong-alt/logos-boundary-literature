# Source Intake Policy

No source ingestion is allowed in this scaffold.

## Acquisition Status Values

- `public_domain`
- `open_license`
- `citation_only`
- `restricted_do_not_ingest`
- `unknown_license`
- `requires_human_source_review`

## Default

```text
ingestion_allowed: false
citation_allowed: false
source_review_required: true
```

## Intake Requirements

Before any source is imported, stored, cited, or summarized as data:

1. identify the work;
2. identify edition and translation;
3. identify license status;
4. identify trust level;
5. identify canon/tradition scope;
6. identify attribution/forgery status;
7. define allowed and forbidden uses;
8. document provenance;
9. pass human source review.

## No Text Import Yet

Do not paste, download, normalize, or stage source texts. This applies to copyrighted texts,
public-domain texts, commentary texts, and short source excerpts unless a later policy explicitly
allows scoped quotation.
