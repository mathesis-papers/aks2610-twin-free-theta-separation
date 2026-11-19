# A different address for every vertex

## A complete fifteen-vertex example

Use short paths $u-a-b-v$, $u-c-d-v$ and long path $y_0=u,\ldots,y_{10}=v$. Write distance to $a$ first and distance to $y_1$ second. The six short-path vertices have addresses:

| Vertex | $u$ | $v$ | $a$ | $b$ | $c$ | $d$ |
|---|---|---|---|---|---|---|
| Address | $(1,1)$ | $(2,4)$ | $(0,2)$ | $(1,3)$ | $(2,2)$ | $(3,3)$ |

The other nine vertices have addresses:

| Vertex | Address | Vertex | Address | Vertex | Address |
|---|---|---|---|---|---|
| $y_1$ | $(2,0)$ | $y_4$ | $(5,3)$ | $y_7$ | $(5,6)$ |
| $y_2$ | $(3,1)$ | $y_5$ | $(6,4)$ | $y_8$ | $(4,6)$ |
| $y_3$ | $(4,2)$ | $y_6$ | $(6,5)$ | $y_9$ | $(3,5)$ |

All $15$ pairs differ. For example, walking from $y_9$ back along the long path to $u$, then to $a$, takes $10$ steps. Going first to $v$ and then along $v-b-a$ takes only $3$. Distance uses the shortest route, rather than the route that looks straightest in a drawing.

## From one example to any long path

For $r\geq6$, the address of an interior long-path vertex is

$$
\begin{gathered}(a_j,b_j),\qquad1\leq j\leq r-1,\\a_j=\min(j+1,r-j+2),\\b_j=\min(j-1,r-j+4).\end{gathered}
$$

The first minimum compares reaching $a$ through $u$ or through $v$. The second compares going directly along the long path to $y_1$ with going through $v$, across a three-edge short path, then from $u$ to $y_1$. These two candidate routes explain each minimum.

In the main family, $r=2h=6k+4$ with $k\geq1$, so $h\geq5$. Addresses in the first part are $(j+1,j-1)$, with first-minus-second coordinate $2$. In the final part they are $(2h-j+2,2h-j+4)$, with difference $-2$. The two middle addresses are $(h+1,h)$ and $(h,h+1)$, with differences $1,-1$. Values change strictly within each outer part, and coordinate differences separate the parts. The six short-path addresses have differences $0,-2,-2,-2,0,0$. Those with difference $-2$ have first coordinates $2,0,1$, whereas the final long-path part has first coordinate at least $3$. Thus there are no collisions with the short paths either.

Two landmarks suffice. Why does one fail? If distances to a single landmark were all distinct integers, the distances across every edge would have to differ by $1$. The three neighbors of a degree-$3$ vertex would have only two possible distances: one less or one more. Two neighbors would therefore have the same distance. Terminal $u$ has degree $3$, so one landmark cannot suffice.

::: {.theorem #theta-geometry title="Geometry of the main theta family" lean="D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaStructure.theta_metric_certificates" mathesis="collected:aks2610-twin-free-theta-separation:2:s1"}
For every natural number $k\geq1$, the graph $\Theta_{3,3,6k+4}$ is connected and twin-free and has metric dimension $2$.
:::

This statement extracts only the geometric part of the manuscript's main theorem. It makes no assertion about spectral multiplicities. The addresses above explain the metric-dimension mechanism.

## Symmetry without twins

Every cycle uses two complete terminal-to-terminal paths, so its length is either $6$ or $r+3$. For every $r\geq2$, there are no triangles or quadrilaterals, and every vertex has degree at least $2$.

Adjacent twins would have a common third neighbor, creating a triangle. Nonadjacent twins would have at least two common neighbors, creating a quadrilateral. Both are impossible. Thus the graph can have a symmetry exchanging its short paths without having twins.

The argument for twin-freeness at every $r\geq2$ is an explanation of the manuscript here. The Lean theorem above states only the case $r=6k+4$, $k\geq1$. The manuscript's full range of lengths appears in the classification remarks later.
