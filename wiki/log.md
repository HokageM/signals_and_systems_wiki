# Log

Append-only record of wiki operations (ingests, saved queries, lint passes).
See `CLAUDE.md` for the entry format.

## [2026-10-25] ingest | signals_1.pdf
- Source: `raw/signals_1.pdf` (27 pages, handwritten)
- Updated: [summaries/signals-1](summaries/signals-1.md), [concepts/signal-classification](concepts/signal-classification.md), [concepts/signal-transformations](concepts/signal-transformations.md), [concepts/even-odd-decomposition](concepts/even-odd-decomposition.md), [concepts/elementary-signals](concepts/elementary-signals.md), [concepts/dirac-impulse](concepts/dirac-impulse.md), [concepts/power-and-energy-of-signals](concepts/power-and-energy-of-signals.md), [concepts/correlation-and-orthogonality](concepts/correlation-and-orthogonality.md), [examples/exercise-1-elementary-and-complex-signals](examples/exercise-1-elementary-and-complex-signals.md), [examples/exercise-power-and-energy-classification](examples/exercise-power-and-energy-classification.md), [examples/exercise-2-orthogonality-and-correlation](examples/exercise-2-orthogonality-and-correlation.md)
- Notes: No unclear handwriting. Added 3 generated plots (elementary signals, si-function/Dirac comb, discrete autocorrelation example) under `wiki/assets/plots/`.

## [2026-10-25] ingest | signals_2.pdf
- Source: `raw/signals_2.pdf` (36 pages, handwritten)
- Updated: [summaries/signals-2](summaries/signals-2.md), [concepts/lti-systems](concepts/lti-systems.md), [concepts/convolution](concepts/convolution.md), [concepts/fourier-series](concepts/fourier-series.md), [concepts/fourier-transform](concepts/fourier-transform.md), [concepts/fourier-transform-properties](concepts/fourier-transform-properties.md), [concepts/fourier-transform-pairs](concepts/fourier-transform-pairs.md), [examples/exercise-convolution-of-lti-systems](examples/exercise-convolution-of-lti-systems.md), [examples/exercise-cyclic-convolution-and-correlation](examples/exercise-cyclic-convolution-and-correlation.md), [examples/exercise-pedestrian-recognition](examples/exercise-pedestrian-recognition.md), [examples/exercise-fourier-series-symmetry-and-equivalence](examples/exercise-fourier-series-symmetry-and-equivalence.md), [examples/exercise-fourier-transform-rect-triangle-and-periodic-signals](examples/exercise-fourier-transform-rect-triangle-and-periodic-signals.md)
- Notes: p.8 (third convolution branch) and p.22 (FS equivalence "proof") flagged as not independently re-derived/verified — see open questions in the lecture summary. Added 4 generated plots under `wiki/assets/plots/` (convolution result, rect/si pair, triangle/si² pair, periodic triangular train spectrum).

## [2026-10-25] ingest | signals_3.pdf
- Source: `raw/signals_3.pdf` (32 pages, handwritten)
- Updated: [summaries/signals-3](summaries/signals-3.md), [concepts/lti-frequency-response](concepts/lti-frequency-response.md), [concepts/phase-and-group-delay](concepts/phase-and-group-delay.md), [concepts/laplace-transform](concepts/laplace-transform.md), [concepts/lti-systems-s-domain](concepts/lti-systems-s-domain.md), [examples/exercise-group-and-phase-delay-allpass-filter](examples/exercise-group-and-phase-delay-allpass-filter.md), [examples/exercise-multicarrier-transmission](examples/exercise-multicarrier-transmission.md), [examples/exercise-fourier-vs-laplace-transform](examples/exercise-fourier-vs-laplace-transform.md), [examples/exercise-inverse-laplace-transform-and-roc](examples/exercise-inverse-laplace-transform-and-roc.md), [examples/exercise-analog-filter-design](examples/exercise-analog-filter-design.md)
- Notes: pp.9–11 (multicarrier exercise) flagged — apparent tension between a general correlation formula and a direct per-period integral; direct computation treated as authoritative. Added 3 generated plots under `wiki/assets/plots/` (filter types, allpass magnitude/phase, analog filter impulse response).

## [2026-10-25] ingest | signals_4.pdf
- Source: `raw/signals_4.pdf` (30 pages, handwritten)
- Updated: [summaries/signals-4](summaries/signals-4.md), [concepts/sampling](concepts/sampling.md), [concepts/discrete-time-fourier-transform](concepts/discrete-time-fourier-transform.md), [concepts/discrete-fourier-transform](concepts/discrete-fourier-transform.md), [concepts/z-transform](concepts/z-transform.md), [examples/exercise-dft-cosine-sequence](examples/exercise-dft-cosine-sequence.md), [examples/exercise-multicarrier-transmission](examples/exercise-multicarrier-transmission.md)
- Notes: Lecture 4 added sampling, DTFT, DFT, and Z-transform material. The inverse-DFT scaling in the multicarrier continuation (p. 22) and the exponential-scaling property in the Z-transform table (p. 26) appear inconsistent with the stated transform definitions; both are flagged rather than silently transcribed.

## [2026-10-25] ingest | signals_5.pdf
- Source: `raw/signals_5.pdf` (17 pages, handwritten)
- Updated: [summaries/signals-5](summaries/signals-5.md), [concepts/digital-filters](concepts/digital-filters.md), [concepts/z-transform](concepts/z-transform.md), [examples/exercise-digital-filters](examples/exercise-digital-filters.md)
- Notes: Added FIR/IIR structures, unit-circle stability, pole-zero examples, and shelving-filter derivation; checked the displayed filter equations and pole/zero locations.

## [2026-10-25] lint | Added missing plots to Lecture 4 pages
- Updated: [concepts/sampling](concepts/sampling.md), [concepts/discrete-fourier-transform](concepts/discrete-fourier-transform.md), [concepts/z-transform](concepts/z-transform.md)
- Notes: Lecture 4/5 ingests had no generated plots. Added 3 (sampling-spectrum aliasing comparison, DFT of a periodic cosine, Z-transform ROC regions) under `wiki/assets/plots/` and embedded them in the relevant concept pages.

## [2026-10-25] ingest | signals_formulas.pdf
- Source: `raw/signals_formulas.pdf` (4 pages, handwritten)
- Updated: [summaries/signals-formulas](summaries/signals-formulas.md)
- Notes: A condensed formula-sheet reference covering the whole module; cross-checked against all existing concept pages with no discrepancies found. No new concept/example pages created (material already covered).

## [2026-10-25] lint | Full wiki health check
- Checked: all relative markdown links, orphan pages/images, frontmatter completeness, index.md coverage of every concept/example/summary page.
- Findings: no broken links; no orphan content pages (only `index.md`/`log.md` themselves have no inbound links, as expected); no missing/incomplete YAML frontmatter; no missing image references; every wiki page is listed in `index.md`.
- Notes: Removed the temporary `temp_render/` scratch directory used for viewing PDF page scans during ingestion (not part of the wiki). No content changes were needed as a result of this lint pass.
