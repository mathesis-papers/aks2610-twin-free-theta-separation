# Two landmarks and two kinds of graph frequency

Imagine a walking map. Junctions are vertices, roads are edges, and each edge takes one step. You know your distances to two chosen landmarks. Do those two numbers determine where you are? A second question seems unrelated: put a real number at each vertex and let a fixed rule combine the numbers at neighboring vertices. How many independent patterns can have the same scaling factor? This paper compares these two questions on one family of maps. Their answers agree for one rule and disagree for the other.

Source paper: Haobo Ma and Wenlin Zhang, [A twin-free answer to Alfuraidan–Khan–Sauras-Altuzarra, arXiv:2610.26875v1, Section 9, Problem 30 (p. 27): a spectral extension of Knor–Sedlar–Škrekovski (2022)](https://doi.org/10.5281/zenodo.24212419), version 2. Manuscript references in this reading refer to this version.

This reading explains public version 2 of the paper by Haobo Ma and Wenlin Zhang, titled *A twin-free answer to Alfuraidan–Khan–Sauras-Altuzarra, arXiv:2610.26875v1, Section 9, Problem 30 (p. 27): a spectral extension of Knor–Sedlar–Škrekovski (2022)*. The authors, in that order, are Haobo Ma (Chrono AI, Singapore) and Wenlin Zhang (National University of Singapore and Chrono AI, Singapore). The paper and this reading use CC BY 4.0. The manuscript is dated 5 November 2026; public version 2 was published on 14 November.

## Start with a road

For five vertices arranged in a path, one endpoint is enough as a landmark. The distances are $0,1,2,3,4$, so everyone has a different address. At a fork, one landmark may confuse vertices equally far away in different directions. A set of landmarks whose distance lists distinguish all vertices is a **resolving set**. The smallest number of landmarks needed is the graph's **metric dimension**, written $\dim G$. This dimension counts landmarks, rather than the spatial dimensions needed to draw the map.

The paper's map has two terminals $u,v$ joined by three paths with disjoint interiors. Two paths have $3$ edges each; the third has $r$ edges. This is $\Theta_{3,3,r}$. Label it

$$
\begin{gathered}
u-a-b-v,\qquad u-c-d-v,\\
u=y_0-y_1-\cdots-y_r=v.
\end{gathered}
$$

Counting the terminals once gives $2+2+2+(r-1)=r+5$ vertices. The parameters count **edges**, rather than interior vertices. Confusing these conventions shifts congruence conditions by one.

Take $r=10$. The map has $15$ vertices. Landmarks at $a$ and $y_1$ distinguish them all. The [next chapter](01-landmarks.md) lists every distance pair, so you can check this yourself.

## Two rules for number patterns

Let $x_w$ be the real number at vertex $w$. Two rules each produce a new number at every vertex $v$:

$$
\begin{aligned}
(Lx)_v&=\deg(v)x_v-\sum_{w\sim v}x_w,\\
(Qx)_v&=\deg(v)x_v+\sum_{w\sim v}x_w.
\end{aligned}
$$

Here $\deg(v)$ counts incident edges, and $w\sim v$ means adjacent. The matrices $L=D-A$ and $Q=D+A$ are called the Laplacian and signless Laplacian; $D$ records degrees and $A$ records adjacency. If a nonzero pattern $x$ becomes $\lambda x$, then $x$ is an eigenvector and $\lambda$ is an eigenvalue. Think of $\lambda$ as a scaling factor; “frequency” is an intuition for these patterns.

The number of independent patterns with the same eigenvalue is its multiplicity. For a single edge, $L$ sends the endpoint pattern $(1,1)$ to $(0,0)$ and sends $(1,-1)$ to $(2,-2)$. Each of the eigenvalues $0,2$ has one independent direction, so the maximum multiplicity is $1$. We write $\operatorname{mm}_L G$ and $\operatorname{mm}_Q G$ for the **largest multiplicity among all eigenvalues**, rather than the multiplicity of the largest eigenvalue.

## Why exclude twins?

Distinct vertices $p,q$ are twins when $N(p)\setminus\{q\}=N(q)\setminus\{p\}$. Ignoring one another, they have identical neighbors. Twins can be adjacent or nonadjacent. They can create both ambiguous distance profiles and repeated number patterns, making some equality examples easier to obtain.

In arXiv:2610.26875v1, Section 9, Problem 30 (p. 27), Alfuraidan, Khan and Sauras-Altuzarra ask whether there are infinitely many pairwise nonisomorphic, connected graphs **without twins** for which exactly one of

$$
\operatorname{mm}_L G=\dim G,\qquad
\operatorname{mm}_Q G=\dim G
$$

holds. Nonisomorphic means that renaming vertices cannot turn one graph into the other.

The paper gives a positive answer. For any integer $k\geq1$, put $r=6k+4$. Its written proof establishes

$$
\begin{gathered}
\dim\Theta_{3,3,r}=\operatorname{mm}_L\Theta_{3,3,r}=2,\\
\operatorname{mm}_Q\Theta_{3,3,r}=1.
\end{gathered}
$$

The two short paths can be exchanged, although their individual interior vertices are not twins. That distinction—symmetry of whole pieces without twins at individual vertices—is the heart of the story. Repeated eigenvalues arise when patterns of two different symmetry types meet at the same value. The [spectral chapter](02-recurrence.md) explains why they meet for $L$ and miss for $Q$.

## A route through the argument

Start with [landmarks and distance certificates](01-landmarks.md), then [symmetry and recurrence](02-recurrence.md). The [classification and two further constructions](03-classification.md) explain small exceptions, earlier literature and the boundaries of the conclusions. [Sources and exact formalization scope](04-sources.md) distinguish the manuscript's written arguments from what the Lean declarations actually state.

The aligned Chinese and English seminar editions follow the same route: landmarks, symmetry, recurrence, classification and evidence scope.

::: {.slides src="seminar"}
Academic presentation: why two landmarks agree with only one spectral multiplicity, with speaker notes.
:::

The short film below introduces the question and the idea behind the argument.

::: {.film src="001-landmarks"}
A narrated introduction to the question and its mathematical mechanism.
:::
