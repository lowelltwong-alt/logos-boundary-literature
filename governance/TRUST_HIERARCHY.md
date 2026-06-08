# Trust Hierarchy

Trust level is not canon status. Trust level describes how a work may be used in this repository
without contaminating canonical Scripture.

## 1. `canonical_scripture_reference_only`

- Description: Canonical Scripture is referenced only through `logos-scripture-graph`; source text is
  not stored here.
- Examples: Genesis, Psalms, John, Romans by Scripture reference only.
- Allowed uses: stable references, cross-repo links, target refs for boundary claims.
- Forbidden uses: storing Scripture text, creating Scripture chunks, changing canonical claims.
- Default retrieval status: reference-only.
- Can influence canonical Scripture? false by default.
- Required review before use: cross-repo contract review.

## 2. `deuterocanonical_tradition_scoped`

- Description: Works whose canon status depends on tradition.
- Examples: Tobit, Judith, Wisdom, Sirach, Baruch, 1-2 Maccabees.
- Allowed uses: tradition-scoped canon discussion, reception history, background, comparison.
- Forbidden uses: universal canonical claims without tradition scope.
- Default retrieval status: scoped retrieval only.
- Can influence canonical Scripture? false by default.
- Required review before use: canon/tradition review.

## 3. `high_trust_noncanonical_background`

- Description: Historically valuable noncanonical works useful for background or reception.
- Examples: 1 Enoch, Jubilees, Didache, Shepherd of Hermas.
- Allowed uses: background, reception, historical comparison, interpretive profile evidence.
- Forbidden uses: treating as Word of God in the default 66-book scope.
- Default retrieval status: background-only with warnings.
- Can influence canonical Scripture? false by default.
- Required review before use: source, tradition, and contamination review.

## 4. `historical_context_source`

- Description: Historical, linguistic, or contextual sources.
- Examples: Josephus, Philo, DSS/Qumran materials.
- Allowed uses: historical context, linguistic background, textual witness discussion.
- Forbidden uses: canonical authority claims.
- Default retrieval status: background-only.
- Can influence canonical Scripture? false by default.
- Required review before use: source-quality and license review.

## 5. `patristic_reception`

- Description: Patristic, conciliar, and early commentary reception.
- Examples: Church Fathers, early commentaries, conciliar reception.
- Allowed uses: reception history, tradition-scoped interpretation, commentary claims.
- Forbidden uses: mutating Scripture records or defaulting to one tradition's reading.
- Default retrieval status: reception-only.
- Can influence canonical Scripture? false by default.
- Required review before use: tradition and source review.

## 6. `heterodox_or_gnostic`

- Description: Works outside orthodox Christian witness by default.
- Examples: Gospel of Thomas, Gospel of Judas, Apocryphon of John.
- Allowed uses: comparison, apologetics, heresy studies, reception history.
- Forbidden uses: normalizing into Christian canon or default doctrine.
- Default retrieval status: quarantined comparison unless reviewed.
- Can influence canonical Scripture? false by default.
- Required review before use: heterodoxy and contamination review.

## 7. `disputed_attribution`

- Description: Works with contested authorship, pseudepigraphy, or uncertain tradition.
- Examples: ancient pseudepigraphal works and contested attributions.
- Allowed uses: attribution study, reception history, source comparison.
- Forbidden uses: claiming authorship as settled without review.
- Default retrieval status: scoped and attribution-warned.
- Can influence canonical Scripture? false by default.
- Required review before use: attribution review.

## 8. `known_forgery_or_fake`

- Description: Known deceptive attribution, modern fake, or fraudulent text.
- Examples: modern fake gospels, fraudulent texts, known deceptive attributions.
- Allowed uses: identification, quarantine, comparison, refutation, contamination defense.
- Forbidden uses: retrieval as trusted background or doctrine.
- Default retrieval status: quarantine.
- Can influence canonical Scripture? false by default.
- Required review before use: forgery evidence review.

## 9. `quarantine_unreviewed`

- Description: Unknown, unsafe, unreviewed, or unclear-provenance material.
- Examples: unsourced internet texts, unknown translations, unclear provenance.
- Allowed uses: triage only.
- Forbidden uses: ingestion, retrieval, claims, interpretation, canonical influence.
- Default retrieval status: unavailable.
- Can influence canonical Scripture? false by default.
- Required review before use: full source review.

## Core Rule

A boundary source can be useful, historically important, high-trust for background, or important for
reception history without being canonical Scripture.
