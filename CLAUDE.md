# Signals and Systems Wiki

## Purpose

Maintain a cumulative, source-grounded wiki for the Signals and Systems module at
TUHH. The primary sources are the user's handwritten lecture summaries and
exercise summaries. Write all wiki content in English, even when a source uses
another language, unless the user asks otherwise.

The wiki is a study aid, not a replacement for the original course material.
Treat the supplied notes as the authority for what was taught in this module.
Do not assume a particular syllabus, notation, convention, or exam requirement
unless it is supported by a source or confirmed by the user.

## Directory layout

Use this layout as the wiki grows; create directories only when needed.

```text
raw/
  lectures/       # Original lecture notes, scans, photos, and PDFs; never edit
  exercises/      # Original exercise notes, scans, photos, and PDFs; never edit
wiki/
  index.md        # Content catalog and entry point
  log.md          # Append-only record of wiki operations
  concepts/       # Topic and method pages
  examples/       # Worked exercise pages
  summaries/      # Lecture or source summaries
  assets/plots/   # Generated plots and their source scripts, when useful
```

Keep raw files unchanged. Put generated and synthesized material under `wiki/`.
Preserve original filenames where possible and refer to sources by relative path.

## Source handling and evidence

- Read each source carefully before summarizing or changing the wiki. For scans
  or handwriting, inspect the relevant image or page directly when needed; OCR
  is a convenience, not definitive evidence.
- If a symbol, equation, sign, unit, label, or word is ambiguous, mark it as
  unclear and ask the user when it affects the interpretation. Never silently
  guess or normalize ambiguous handwritten notation.
- Cite claims, definitions, equations, and exercise solutions with links to the
  original source and a page number, section, or other locator when available.
  Example: `[Lecture 2, p. 3](../../raw/lectures/lecture-02.pdf#page=3)`.
- Preserve the source's notation and state its conventions (for example, Fourier
  transform definition, frequency units, or sign convention) when known. If
  different sources use different conventions, explain the difference rather
  than merging them.
- Separate source-backed statements from explanations, derivations, and
  interpretations added by the wiki. Label uncertain or inferred details.
- Do not add external facts or browse for sources unless the user asks. If the
  notes conflict or appear incomplete, record the discrepancy and ask rather
  than resolving it by assumption.

## Page conventions

Use Markdown with LaTeX math (`$...$` inline and `$$...$$` for displayed
equations). Use relative Markdown links so pages remain navigable outside
Obsidian. Prefer descriptive filenames in lowercase kebab-case.

Add YAML frontmatter to new wiki pages:

```yaml
---
title: "Page title"
type: concept
sources:
  - "../../raw/lectures/lecture-01.pdf"
tags:
  - signals-and-systems
---
```

Use `concept`, `example`, or `summary` as the applicable `type` value and add
source paths actually used. A page should normally include:

1. A concise explanation of the topic or purpose.
2. Key definitions, equations, assumptions, and notation.
3. A worked example or interpretation where supported by the notes.
4. Source citations close to the relevant claims.
5. Links to related concepts, summaries, and examples.
6. Open questions or unclear source details, if any.

### Concept pages

Explain what a concept means, how it connects to other course topics, and when
its equations or methods apply. Define variables and state assumptions. Do not
present a formula without its relevant conditions or conventions if those are
known.

### Exercise pages

Show the problem statement or a faithful concise paraphrase, source reference,
step-by-step reasoning, and final result. Distinguish the source's solution
from a solution derived by the wiki. Check units, limiting cases, and
intermediate reasoning where applicable; flag any uncertainty instead of
claiming an unchecked result is verified.

### Visualizations

Add a plot when it materially clarifies a signal, system response, transform,
sampling effect, or worked example. Keep plots mathematically consistent with
the stated definitions, units, and parameter values. Save generated images in
`wiki/assets/plots/`, include a descriptive caption and link from the page, and
keep the plotting script alongside the image when practical so the figure is
reproducible. Do not create decorative or unsupported plots.

## Operations

### Ingesting a source

Process sources one at a time unless the user requests batch processing.

1. Identify the source type and inspect its contents; do not modify the raw
   file.
2. Summarize its main ideas, definitions, equations, conventions, and examples
   in English, preserving important detail and noting unclear handwriting.
3. Create or update the relevant summary, concept, and exercise pages. Check
   existing pages first and integrate the material rather than duplicating it.
4. Add accurate source citations and links between related pages.
5. Update `wiki/index.md` and append an entry to `wiki/log.md`.
6. Report what changed and call out ambiguities, conflicts, or questions for
   the user.

### Answering questions

Start with `wiki/index.md`, then read the relevant wiki pages and verify
important claims against their cited source notes. Answer in English with
citations. Make clear when an answer is not covered by the available sources.
If the result is a durable explanation, derivation, comparison, or study aid,
offer it as a new wiki page only when appropriate to the user's request; link
and index it if created.

### Maintaining the wiki

When asked to lint or review the wiki, check for broken links, missing or
incorrect citations, inconsistent notation or conventions, contradictions,
stale summaries, orphan pages, and relevant topics that lack a page. Report
uncertain findings rather than silently rewriting source-backed claims. Make
repairs that are directly supported by the sources, then update the index and
append a log entry.

## Index and log

`wiki/index.md` is the content-oriented catalog. Keep it organized by page
type (summaries, concepts, examples), with a link and a one-line description
for every wiki page. Update it whenever pages are created, renamed, or removed.

`wiki/log.md` is chronological and append-only. Add one entry for each ingest,
substantive query saved to the wiki, or lint pass, using this format:

```markdown
## [YYYY-MM-DD] ingest | Source title
- Source: `raw/lectures/lecture-01.pdf`
- Updated: [[summaries/lecture-01]], [[concepts/linear-time-invariant-systems]]
- Notes: Briefly record important ambiguities or changes.
```

Use the operation name `query` or `lint` instead of `ingest` where applicable.
Log links are relative to `wiki/log.md`; for example:

```markdown
## [2026-10-25] ingest | Lecture 1
- Source: `raw/lectures/lecture-01.pdf`
- Updated: [Lecture 1 summary](summaries/lecture-01.md), [LTI systems](concepts/linear-time-invariant-systems.md)
- Notes: No unclear notation.
```

Do not rewrite earlier log entries except to correct an obvious factual or
formatting error.
