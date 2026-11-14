# A twin-free answer to Problem 30

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of
Singapore; ChronoAI Pte Ltd, Singapore), 5 November 2026.

For every integer `k >= 1`, the graph with three internally disjoint paths of
edge lengths `3, 3, 6k+4` is connected and twin-free. Its metric dimension and
maximum Laplacian eigenvalue multiplicity are two; its signless Laplacian has
simple spectrum. This answers Problem 30 in Alfuraidan, Khan and
Sauras-Altuzarra, arXiv:2610.26875v1, page 27, in the Laplacian-equality direction.
The exact posing locator is Section 9, Problem 30, page 27 of
arXiv:2610.26875v1. This spectral extension of Knor, Sedlar and Škrekovski
(2022) classifies both maximum multiplicities of `Theta(3,3,r)` for every
edge length `r >= 2`. For `r >= 3` the spectral rule is modulo six;
`r = 2` has the repeated Laplacian eigenvalues `3-sqrt(2), 3+sqrt(2)`.
The metric dimension is three at `r = 3,5` and two otherwise, as in their
Theorems 8 and 14 (arXiv:2203.07335v1). Exactly one equality holds precisely
when `r = 2` or `r = 4 mod 6`, always in the Laplacian direction.
The signless-only direction is impossible in this whole subfamily.
The aggregate values at `r = 2` were already listed in the posing paper's
Table 2, row 2, p. 23; the note supplies its exact characteristic factors.
The multiplicity of the signless eigenvalue 2 equals one precisely when
`r = 1 mod 4`; this is a specialization of Paone–Paone (2026), Corollary 8.1.
Attaching one path of any positive length to every vertex of `K_{1,3,3}`
gives `(dim,mm_L,mm_Q)=(4,4,5)`; the same construction on `K_2 join (2K_2)`
gives `(3,2,3)`. Both families are connected and twin-free. The note proves
this consequence of known rooted-product results and the source's base values.
A known modular lower bound from Belmonte et al. (2016) is also reproved.

## Files

- `note.tex`: focused written proofs and ten scientific references.
- `note.pdf`: readable note, supplied alongside the source archive.
- `verify.py`: symbolic identities, all 24 singular systems, 39 theta cases and eight rooted-path cases.
- `checks.json`: expected exact output of `verify.py`.
- `metadata.json`: title, creators, license and scientific source links.
- `requirements.txt`: computational dependency.

## Build

Build the PDF with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, run `pdflatex note.tex` twice with the standard AMS, geometry,
booktabs, array, hyperref, fontenc and lmodern packages installed. The bibliography
is embedded, so BibTeX is unnecessary.

For the exact checks use Python 3.10 or later:

```sh
python3 -m pip install -r requirements.txt
python3 verify.py --output regenerated-checks.json
python3 -c "from pathlib import Path; assert Path('checks.json').read_bytes() == Path('regenerated-checks.json').read_bytes()"
```

The finite cases cover every `r = 2,...,40`, and therefore include the original
family at `k = 1,...,6`, of orders `15,21,27,33,39,45`. Graph
connectivity, twin-freeness and resolving distances are exact integer checks.
Every pair of vertices is tested as a landmark set at `r = 3,5`, where
a resolving triple is supplied. The other cases use the pair `(a,y_1)`.
Characteristic polynomials and their greatest common divisors with their
derivatives are computed over the rationals. The script also checks the two
endpoint factorizations and all 24 singular boundary systems symbolically.
The exceptional length-two factors and the multiplicity at the signless
eigenvalue 2 are checked as well. The all-parameter spectral conclusions
follow from the written proof, independently of these finite cases.
The rooted-path cases use both bases and paths of one through four edges,
checking leaf resolving sets, twin-freeness, connectivity and exact multiplicities.

## Scientific coverage

`TwinFreeThetaSeparation.result` in the pinned
[Lean file](https://github.com/the-omega-institute/trureturing/blob/d9bb8a406783c5222849b798f3c2ab738f653d75/D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaSeparation.lean)
has as its conclusion existence of the connected twin-free separating family and pairwise
nonisomorphism, with witnesses `Theta(3,3,6k+4)`, `k >= 1`.
The explicit distance certificates, repeated-eigenvalue classification and
extension to all `r >= 2` have written proofs in the note; the exceptional
metric dimensions use Knor–Sedlar–Škrekovski (2022), Theorem 8.
Problem 29 is settled for this entire subfamily, not for all theta graphs.
The note's coverage table distinguishes the affirmative answer to Problem 30,
partial answers to Problems 28,29,32, prior results, and Problems 31,33.
The rooted-path construction uses one path per root, not the at-least-two
copies specified in Problem 33, so that repeated-branch problem remains separate.

## References

- Alfuraidan, Khan and Sauras-Altuzarra (2026), Section 9, p. 27:
  https://arxiv.org/abs/2610.26875v1.
- Knor, Sedlar and Škrekovski (2022), Theorems 8 and 14:
  https://arxiv.org/abs/2203.07335v1; journal DOI 10.3390/math10142411.
- Benakli, Froitzheim and Martinez (2025), Theorem 4.4, p. 11,
  a later alternative metric-dimension proof, with internal-vertex parameters
  `(2,2,r-1)`, after reordering: https://arxiv.org/abs/2510.12100v1.
- Paone and Paone (2026), version 1.0, Corollary 8.1, pp. 10–11:
  https://doi.org/10.5281/zenodo.21744051.
- Bahmani and Kiani (2015/2016), Corollary 16 and Example 17, periodicity
  at 1 and 3: https://arxiv.org/abs/1512.08265v5.
- Liu and Lu (2014), Proposition 2.6 and equations (2.1), (2.3), theta
  characteristic polynomials: https://arxiv.org/abs/1407.5255v2.
- Jannesari (2023), Theorem 2.2, metric dimension with one leaf at each root:
  https://doi.org/10.5666/KMJ.2022.63.1.123.
- Feng and Wang (2012), Proposition 2.10, longer pendant paths:
  https://arxiv.org/abs/1211.1432v1.
- Cardoso, Martins, Robbiano and Rojo (2013), Theorem 2.1, rooted-product spectra:
  https://doi.org/10.13001/1081-3810.1681.
- Belmonte, Fomin, Golovach and Ramanujan (2016), Section 4, Lemma 7,
  the modular lower bound: https://arxiv.org/abs/1602.02610v1.

License: Creative Commons Attribution 4.0 International (CC BY 4.0),
https://creativecommons.org/licenses/by/4.0/.
