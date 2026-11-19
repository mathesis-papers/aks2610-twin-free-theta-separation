# Exact conclusions, sources and contribution routes

## Existence and a complete classification are different statements

::: {.theorem #infinite-separation title="Infinitely many twin-free separation examples" lean="D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaSeparation.result" mathesis="collected:aks2610-twin-free-theta-separation:2:s2"}
There exist a sequence of orders $(n_i)_{i\in\mathbb N}$ and simple graphs $G_i$ on $\{0,\ldots,n_i-1\}$ such that every $G_i$ is connected and twin-free and satisfies

$$
\begin{gathered}\bigl(\operatorname{mm}_L G_i=\dim G_i\\\text{and}\quad\operatorname{mm}_Q G_i\ne\dim G_i\bigr)\\\text{or}\\\bigl(\operatorname{mm}_Q G_i=\dim G_i\\\text{and}\quad\operatorname{mm}_L G_i\ne\dim G_i\bigr).\end{gathered}
$$

Moreover, for every $i\ne j$ there is no graph isomorphism from $G_i$ to $G_j$.
:::

This matches the expanded `claim` proved by the public declaration `TwinFreeThetaSeparation.result`. It is an existential consequence of manuscript Corollary 2, rather than a literal formalization of that corollary's assertion about specified graphs $G_k$. The proof chooses $n_i=6(i+1)+9$ and $G_i=\Theta_{3,3,6(i+1)+4}$, corresponding to $k=i+1\geq1$, and uses the first branch above. The **conclusion itself** does not name these witnesses, the direction, the exact maximum multiplicities or the list of repeated eigenvalues. A witness used inside a proof must not be mistaken for a conclusion stating all its properties.

The geometric declaration `theta_metric_certificates` explicitly proves connectivity, twin-freeness and metric dimension $2$ for each natural number $k\geq1$. That is why it has its own theorem block. These two results cover the geometric and existential conclusions; the complete spectral classification has a separate written argument.

## Reading the evidence

| Content | Basis and scope here |
|---|---|
| Connectivity, twin-freeness and metric dimension $2$ at $r=6k+4$ | Geometric Lean declaration, requiring $k\geq1$ |
| Existence of infinitely many pairwise nonisomorphic graphs with exactly one equality | Existential Lean declaration, without a spectral list |
| Only $1,3$ repeated in the main family; classification for all lengths | Manuscript written proofs, presented as attributed remarks with shared requests |
| Eigenvalue $2$ of $Q$, both rooted-path families, module bound | Manuscript proofs and credited prior literature, with separate requests |
| Exact calculations reported for $2\leq r\leq40$ | Finite supporting evidence, rather than a proof for all parameters |

The finite calculations illustrate the written argument. The proofs for all parameters come from the recurrence and endpoint equations, with the precise Lean scope listed above.

## What is answered, and what remains outside the scope?

Problem 30 asks only for an infinite family in one separation direction. The main theta family already gives a positive answer; the rooted-path corollary additionally supplies both directions. The complete theta classification answers the congruence question of Problem 29 within $\Theta_{3,3,r}$, without classifying all triples of path lengths.

The paper does not characterize equality for all connected graphs (Problem 28), improve the exponential counting lower bound by graph order (Problem 31), or give a general spectral-equality criterion for partitions (Problem 32). The module bound and the equitable partition from the short-path exchange are specific contributions. Attaching one path per root also differs from the multiple branches required in Problem 33. In particular, the absence of signless-only examples in this theta subfamily is not an absence theorem for all twin-free graphs: the second rooted-path family demonstrates that direction.

## The paper and its predecessors

The [public Mathesis record](https://mathesis-omega-research.apps.chrono-ai.fun/papers/aks2610-twin-free-theta-separation?version=2) identifies version 2, its authors and licence. The fixed-version [Lean existence source](https://github.com/the-omega-institute/trureturing/blob/d9bb8a406783c5222849b798f3c2ab738f653d75/D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaSeparation.lean) and [geometry source](https://github.com/the-omega-institute/trureturing/blob/d9bb8a406783c5222849b798f3c2ab738f653d75/D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaStructure.lean) allow readers to inspect the public formalization used by the manuscript.

| Source | Role in this paper |
|---|---|
| Alfuraidan–Khan–Sauras-Altuzarra, *Metric dimension and maximum eigenvalue multiplicity of graph Laplacians*, [arXiv:2610.26875v1](https://arxiv.org/abs/2610.26875v1) | Section 9, Problem 30; the $r=2$ graph in Table 2; base graphs for rooted paths |
| Knor–Sedlar–Škrekovski, *Remarks on the vertex and the edge metric dimension of 2-connected graphs* (2022), [10.3390/math10142411](https://doi.org/10.3390/math10142411) | Metric classification in arXiv Theorems 8, 14; the metric classification is prior work |
| Benakli–Froitzheim–Martinez (2025), [arXiv:2510.12100v1](https://arxiv.org/abs/2510.12100v1), Theorem 4.4 | A later alternative metric proof, using interior-vertex parameters |
| Bahmani–Kiani, [arXiv:1512.08265v5](https://arxiv.org/abs/1512.08265v5), Corollary 16 | Periodicity at specific eigenvalues $1,3$, rather than exclusion of other repetitions |
| Liu–Lu, [arXiv:1407.5255v2](https://arxiv.org/abs/1407.5255v2), Proposition 2.6 | Earlier theta characteristic-polynomial formulas |
| A. Paone–M. Paone, *Line-graph inertia of roses and generalized theta graphs*, v1.0 (2026), [10.5281/zenodo.21744051](https://doi.org/10.5281/zenodo.21744051), Corollary 8.1 | Prior formula for signless eigenvalue $2$ |
| Jannesari (2023), [10.5666/KMJ.2022.63.1.123](https://doi.org/10.5666/KMJ.2022.63.1.123), Theorem 2.2 | The one-leaf metric criterion |
| Feng–Wang, [arXiv:1211.1432v1](https://arxiv.org/abs/1211.1432v1), Proposition 2.10 | Metric tools for longer paths on diameter-two bases |
| Cardoso–Martins–Robbiano–Rojo (2013), [10.13001/1081-3810.1681](https://doi.org/10.13001/1081-3810.1681), Theorem 2.1 | Spectral blocks for rooted products |
| Belmonte–Fomin–Golovach–Ramanujan, [arXiv:1602.02610v1](https://arxiv.org/abs/1602.02610v1), Section 4, Lemma 7 | The module metric lower bound |

## Contribute through the same shared requests

The focused scopes are the [precise main-family spectrum](https://github.com/the-omega-institute/trureturing-requests/issues/39), [all-length classification](https://github.com/the-omega-institute/trureturing-requests/issues/40), [eigenvalue two](https://github.com/the-omega-institute/trureturing-requests/issues/41), [rooted-path construction](https://github.com/the-omega-institute/trureturing-requests/issues/42) and [module bound](https://github.com/the-omega-institute/trureturing-requests/issues/43). They retain original authors, prior work, exact version and scope. Coordinate the part you intend to tackle on the corresponding request, then follow the [upstream contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md), submitting a focused PR from a contributor fork directly to upstream `dev`. After formalization is merged, statements still need comparison. Issue closure or passing CI does not cover the entire paper or award platform credit or receipts.
