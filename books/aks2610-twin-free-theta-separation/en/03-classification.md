# Six residues, small exceptions and two extensions

## How does length control repetition?

Substitute the periodic sequences into the endpoint conditions and check the six residues. The table lists **repeated eigenvalues**, rather than the full spectrum. An empty set means every eigenvalue is simple. Every listed eigenvalue is exactly double.

::: {.remark #residue-classification title="Manuscript Corollary 3: the modulo-six classification" mathesis="collected:aks2610-twin-free-theta-separation:2:s3"}
For every integer $r\geq6$, $\Theta_{3,3,r}$ is connected and twin-free and has metric dimension $2$. Corollary 3 in Section 3.3 proves the following repeated eigenvalues and maximum multiplicities:

| $r\bmod6$ | Repeated in $L$ | Repeated in $Q$ | $\operatorname{mm}_L$ | $\operatorname{mm}_Q$ |
|---|---|---|---|---|
| $0$ | $3$ | $1$ | $2$ | $2$ |
| $1$ | $3$ | $3$ | $2$ | $2$ |
| $2$ | $\varnothing$ | $\varnothing$ | $1$ | $1$ |
| $3$ | $1,3$ | $1,3$ | $2$ | $2$ |
| $4$ | $1,3$ | $\varnothing$ | $2$ | $1$ |
| $5$ | $\varnothing$ | $\varnothing$ | $1$ | $1$ |

Every listed value is double and every other eigenvalue is simple. Thus both equalities hold in residues $0,1,3$, neither in residues $2,5$, and only the Laplacian equality in residue $4$. The [shared all-length classification request](https://github.com/the-omega-institute/trureturing-requests/issues/40) includes this restricted range.
:::

Why not copy the $L$ column to obtain the $Q$ column? Because $\lambda=2-et$: at $e=1$, $t=1$ means $\lambda=1$; at $e=-1$, it means $\lambda=3$. The endpoint equations also contain $e$, so they must be solved again, rather than merely relabeled.

The distance argument also needs its own check. For even $r\geq6$, the two middle addresses have differences $1,-1$. For odd $r=2h+1\geq7$, there is one middle address $(h+1,h+1)$. Its coordinates are at least $4$, so it differs from the short-path addresses $(1,1),(2,2),(3,3)$. The two outer parts retain differences $2,-2$ and remain collision-free.

## Small graphs need separate treatment

::: {.remark #all-lengths title="Manuscript Corollary 4: the complete statement for every length" mathesis="collected:aks2610-twin-free-theta-separation:2:s4"}
Corollary 4 in Section 3.3 proves that $\Theta_{3,3,r}$ is connected and twin-free for every integer $r\geq2$. Its metric dimension is $3$ for $r=3,5$, and $2$ otherwise. The spectral table above holds for all $r\geq3$. At $r=2$, the only repeated Laplacian eigenvalues are $3-\sqrt2,3+\sqrt2$, each double, and the signless spectrum is simple.

Consequently exactly one equality holds if and only if $r=2$ or $r\equiv4\pmod6$, always in the Laplacian direction. Both hold if and only if $r\geq6$ and $r\equiv0,1,3\pmod6$. Neither holds in the remaining cases. No graph in this entire subfamily separates in the signless direction. [All-length classification request](https://github.com/the-omega-institute/trureturing-requests/issues/40).
:::

At $r=3,5$, the maximum spectral multiplicities are still $2,2$, but metric dimension is $3$, so both equalities fail. These metric exceptions come from the existing classification of Knor–Sedlar–Škrekovski (2022). The aggregate values $(\dim,\operatorname{mm}_L,\operatorname{mm}_Q)=(2,2,1)$ for $r=2$ already appear in Table 2, second row, of Alfuraidan–Khan–Sauras-Altuzarra.

The manuscript refines the length-two spectrum using characteristic polynomials:

$$
\begin{aligned}
\chi_L(z)&=z(z-1)(z-3)(z^2-6z+7)^2,\\
\chi_Q(z)&=(z-1)(z-3)(z^2-4z+1)\\
&\quad\cdot(z^3-8z^2+17z-8).
\end{aligned}
$$

The squared factor supplies the double roots $3\pm\sqrt2$. The quadratic and cubic factors of $Q$ have nonzero discriminants $12,316$. The remainder of the cubic modulo the quadratic is $-4$, so they have no common root. Neither vanishes at $1,3$. Thus $\chi_Q$ has no repeated root.

## Follow eigenvalue two separately

::: {.remark #signless-two title="Manuscript Corollary 5: a Paone–Paone specialization" mathesis="collected:aks2610-twin-free-theta-separation:2:s5"}
For every integer $r\geq2$, the multiplicity of eigenvalue $2$ in $Q(\Theta_{3,3,r})$ is $1$ when $r\equiv1\pmod4$ and $0$ otherwise. Corollary 5 in Section 3.3 is the $(3,3,r)$ specialization of Paone–Paone (2026), Corollary 8.1. [Formalization request for this specialization](https://github.com/the-omega-institute/trureturing-requests/issues/41).
:::

Put $e=-1,t=0$ into the recurrence to get $A,s,-A,-s,\ldots$, with period four. The short paths give $C=-A$, $B=-D_0$, $s=-A+2D_0$. Of the four residue cases for the endpoint equations, only residue $1$ leaves one free parameter; the others force the zero pattern. The antisymmetric part has only eigenvalues $1,3$ and contributes nothing at $2$. This modulo-four statement follows one possible simple eigenvalue; the modulo-six **repeated-root** classification answers a different question.

## Beyond theta graphs: obtain both directions

Attach an identical tail to every vertex of a base graph: a path of $t$ edges with one endpoint identified with the base vertex. Here $t\geq1$, and each root receives **one** path.

::: {.remark #rooted-paths title="Manuscript Corollary 6: two rooted-path families" mathesis="collected:aks2610-twin-free-theta-separation:2:s6"}
For each integer $t\geq1$, construct $H_t$ from $H$ as above. If $H=K_{1,3,3}$, then $(\dim H_t,\operatorname{mm}_L H_t,\operatorname{mm}_Q H_t)=(4,4,5)$. If $H=K_2\vee(2K_2)$, the triple is $(3,2,3)$. Each construction gives an infinite family of pairwise nonisomorphic connected twin-free graphs, covering the two separation directions. Corollary 6 in Section 4 specializes prior rooted-product and base-graph results. [Rooted-path construction request](https://github.com/the-omega-institute/trureturing-requests/issues/42).
:::

The graph $K_{1,3,3}$ has parts of sizes $1,3,3$, with no edges within a part and every edge between different parts. The graph $2K_2$ consists of two disjoint edges. To obtain $K_2\vee(2K_2)$, add two joined vertices, each adjacent to all four original vertices.

Two quantities are preserved. For distances, move a base resolving set to the corresponding tail tips. The distance from $(v,j)$ to $(b,t)$ is $t-j$ if $v=b$, and $j+t+d_H(v,b)$ otherwise. For the first base choose two vertices from each large part; the remaining base profiles are $1111,2211,1122$. For the second choose one vertex from each of its three twin pairs; the remaining profiles are $111,112,121$. No two profiles differ by a nonzero constant vector, so changing height $j$ cannot hide the base vertex's identity. Conversely, projecting any resolving set to the base resolves all roots and gives the matching lower bound.

For spectra, each base eigenvalue $\mu$ produces a tridiagonal block $X(P_{t+1})+\mu E_{00}$, for $X=L,Q$. Row recurrence makes each block's spectrum simple. Its polynomial is $F(z)-\mu R(z)$. Consecutive endpoint minors have no common zero: propagating a common zero through their recurrence would eventually make the constant minor $1$ vanish. Thus blocks for different $\mu$ also have disjoint spectra, preserving the maximum multiplicity. The bases have $(\operatorname{mm}_L,\operatorname{mm}_Q)=(4,5)$ and $(2,3)$. After attachment, roots have degree at least $3$ and distinct tail neighbors. Nonroots lie on acyclic tails, and distinct leaves have distinct parents. These facts exclude twins. Orders $7(t+1)$ and $6(t+1)$ strictly increase within each family.

Credit the base examples to Alfuraidan–Khan–Sauras-Altuzarra, the metric tools to Jannesari and Feng–Wang, and the spectral blocks to Cardoso–Martins–Robbiano–Rojo. The paper supplies an explicit specialization to these two families; these tools are not all new discoveries.

## A separate lower bound for landmarks

A **module** $M$ is a nonempty proper vertex subset such that every outside vertex is adjacent to all of $M$ or to none of it. In a connected graph, an outside vertex has the same distance to every member of a module, so outside landmarks cannot distinguish its members. Let $\rho(M)$ be the minimum number of landmarks inside $M$ that distinguish its vertices using induced distances capped at $2$, with disconnected pairs also assigned $2$. A singleton has $\rho=0$.

::: {.remark #module-bound title="Manuscript Corollary 7: a lower bound from disjoint modules" mathesis="collected:aks2610-twin-free-theta-separation:2:s7"}
For a finite simple connected graph $G$ and any finite list of pairwise disjoint nonempty proper modules $M_1,\ldots,M_s$, one has $\dim G\geq\sum_i\rho(M_i)$. Corollary 7 in Section 5 restates and proves the prior bound implicit in Belmonte–Fomin–Golovach–Ramanujan (2016), Section 4, Lemma 7. [Module-bound request](https://github.com/the-omega-institute/trureturing-requests/issues/43).
:::

Every proper module in a connected graph has an outside vertex adjacent to all its members, so nonadjacent members have distance at most $2$. Any resolving set must supply at least $\rho(M_i)$ landmarks inside $M_i$. Disjointness is what permits adding these counts. A twin class of size $m$ gives the familiar bound $m-1$. This is a distance lower bound, rather than a general test for spectral equality.
