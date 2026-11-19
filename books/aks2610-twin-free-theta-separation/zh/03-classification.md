# 六种余数、小例外与两种延伸

## 长度怎样控制重复？

把周期序列代回两端条件，就能逐一检查六种余数。下面的表列的是**重复的特征值**，并非完整的谱；空集表示全部特征值单重。每个列出的特征值都恰好二重。

::: {.remark #residue-classification title="原文推论 3：长路的模六分类" mathesis="collected:aks2610-twin-free-theta-separation:2:s3"}
对每个整数 $r\geq6$，$\Theta_{3,3,r}$ 连通、无孪生点，度量维数为 $2$。原文第 3.3 节推论 3 证明其重复特征值与最大重数为：

| $r\bmod6$ | $L$ 中重复值 | $Q$ 中重复值 | $\operatorname{mm}_L$ | $\operatorname{mm}_Q$ |
|---|---|---|---|---|
| $0$ | $3$ | $1$ | $2$ | $2$ |
| $1$ | $3$ | $3$ | $2$ | $2$ |
| $2$ | $\varnothing$ | $\varnothing$ | $1$ | $1$ |
| $3$ | $1,3$ | $1,3$ | $2$ | $2$ |
| $4$ | $1,3$ | $\varnothing$ | $2$ | $1$ |
| $5$ | $\varnothing$ | $\varnothing$ | $1$ | $1$ |

每个列出值二重，其他值单重。于是余数 $0,1,3$ 时两个等式都成立，余数 $2,5$ 时都不成立，余数 $4$ 时只有拉普拉斯等式成立。[全长度分类的共享请求](https://github.com/the-omega-institute/trureturing-requests/issues/40)也涵盖这项限制范围的结果。
:::

为何 $Q$ 的 $1,3$ 列不能直接照搬 $L$？因为 $\lambda=2-et$：$e=1$ 时 $t=1$ 对应 $\lambda=1$；$e=-1$ 时 $t=1$ 对应 $\lambda=3$。端点方程也含有 $e$，所以不仅要交换名称，还要重新解方程。

度量部分也需单独检查。偶数 $r\geq6$ 的两中间地址差为 $1,-1$；奇数 $r=2h+1\geq7$ 时，出现一个中间地址 $(h+1,h+1)$。它的坐标至少为 $4$，不等于短路上的 $(1,1),(2,2),(3,3)$。其余两段地址差为 $2,-2$，继续无碰撞。

## 小图不能简单套表

::: {.remark #all-lengths title="原文推论 4：所有长度的完整结论" mathesis="collected:aks2610-twin-free-theta-separation:2:s4"}
原文第 3.3 节推论 4 证明：所有整数 $r\geq2$ 的 $\Theta_{3,3,r}$ 连通且无孪生点。度量维数在 $r=3,5$ 时为 $3$，其余情况为 $2$。前表的谱结论对所有 $r\geq3$ 成立。$r=2$ 时，$L$ 只有 $3-\sqrt2,3+\sqrt2$ 重复，各二重，而 $Q$ 的谱单重。

因此恰好一个等式成立当且仅当 $r=2$ 或 $r\equiv4\pmod6$，且均为拉普拉斯方向。两个等式都成立当且仅当 $r\geq6$ 且 $r\equiv0,1,3\pmod6$；其余情况都不成立。整个子族没有无符号拉普拉斯方向独有的例子。[全长度分类请求](https://github.com/the-omega-institute/trureturing-requests/issues/40)。
:::

$r=3,5$ 的谱最大重数仍是 $2,2$，但度量维数是 $3$，所以两个等式都失败。这两个度量例外来自 Knor–Sedlar–Škrekovski（2022）的既有分类，不是本文首次发现。$r=2$ 的总量 $(\dim,\operatorname{mm}_L,\operatorname{mm}_Q)=(2,2,1)$ 也已出现在 Alfuraidan–Khan–Sauras-Altuzarra 的表 2 第二行。

原文用以下特征多项式细化长度二的谱：

$$
\begin{aligned}
\chi_L(z)&=z(z-1)(z-3)(z^2-6z+7)^2,\\
\chi_Q(z)&=(z-1)(z-3)(z^2-4z+1)\\
&\quad\cdot(z^3-8z^2+17z-8).
\end{aligned}
$$

平方因子给出二重根 $3\pm\sqrt2$。$Q$ 的二次与三次因子的判别式分别为 $12,316$，都非零；三次因子除以二次因子的余数为 $-4$，故没有共同根。它们也不在 $1,3$ 消失。因此 $\chi_Q$ 没有重根。

## 单独追踪特征值二

::: {.remark #signless-two title="原文推论 5：Paone–Paone 的特例" mathesis="collected:aks2610-twin-free-theta-separation:2:s5"}
对每个整数 $r\geq2$，$Q(\Theta_{3,3,r})$ 在特征值 $2$ 处的重数在 $r\equiv1\pmod4$ 时为 $1$，其余为 $0$。原文第 3.3 节推论 5 是 Paone–Paone（2026）推论 8.1 的 $(3,3,r)$ 特例。[该特例的形式化请求](https://github.com/the-omega-institute/trureturing-requests/issues/41)。
:::

把 $e=-1,t=0$ 代入递推，序列成为 $A,s,-A,-s,\ldots$，四步重复。短路给出 $C=-A$、$B=-D_0$、$s=-A+2D_0$。检查四种余数的端点条件，仅余数 $1$ 留下一个自由参数；其余只能全零。反对称部分只有特征值 $1,3$，不贡献 $2$。注意，这个模四结论只追踪一个可能的单重特征值，与模六的**重根**分类回答不同问题。

## 离开 theta 族，两种方向都能实现

给底图的每个点接一条同样长的“尾巴”：一条 $t$ 边的路，其中一个端点与原顶点重合。$t\geq1$，每个根只接**一条**路。

::: {.remark #rooted-paths title="原文推论 6：挂路径的两个无限族" mathesis="collected:aks2610-twin-free-theta-separation:2:s6"}
对每个整数 $t\geq1$，按上法由 $H$ 构造 $H_t$。若 $H=K_{1,3,3}$，则 $(\dim H_t,\operatorname{mm}_L H_t,\operatorname{mm}_Q H_t)=(4,4,5)$；若 $H=K_2\vee(2K_2)$，则三元组为 $(3,2,3)$。两者分别给出连通、无孪生点且两两不同构的无限族，涵盖两个分离方向。原文第 4 节推论 6 专门化了既有根积与底图结果。[挂路径构造请求](https://github.com/the-omega-institute/trureturing-requests/issues/42)。
:::

$K_{1,3,3}$ 把点分成大小 $1,3,3$ 的三组，同组不相连，异组全部相连。$2K_2$ 是两条不相交的边；$K_2\vee(2K_2)$ 再加入一条边上的两个点，并将它们分别连接到原来四个点。

证明包含两种“保持”。距离方面，把底图路标移到对应尾巴的末端。对顶点 $(v,j)$，到末端 $(b,t)$ 的距离在 $v=b$ 时为 $t-j$，否则为 $j+t+d_H(v,b)$。第一个底图可选两大组各两个点，剩余底图距离清单为 $1111,2211,1122$；第二个底图可从三个孪生对各选一个点，剩余清单为 $111,112,121$。任意两份清单的差都不是非零常数向量，因此高度 $j$ 不会掩盖底点身份。反向把任意路标投影到底图，会分辨所有根，给出相同下界。

谱方面，底图的每个特征值 $\mu$ 产生一个三对角块 $X(P_{t+1})+\mu E_{00}$，$X=L,Q$。行递推使每个块谱单重。其多项式写成 $F(z)-\mu R(z)$，相邻端点子式无共同根，否则递推最终会迫使常数子式 $1$ 为零；所以不同 $\mu$ 的块也无共同特征值，原最大重数得以保持。底图的 $(\operatorname{mm}_L,\operatorname{mm}_Q)$ 分别为 $(4,5)$ 与 $(2,3)$。挂路后的根有度数至少 $3$ 且各自有不同的尾巴邻居；非根点在无圈尾巴上，叶子的父点也互异。这些性质排除孪生点。阶数分别为 $7(t+1)$、$6(t+1)$，各族内部随 $t$ 严格增加。

底图例子归于 Alfuraidan–Khan–Sauras-Altuzarra；度量的既有工具来自 Jannesari 与 Feng–Wang；谱分块来自 Cardoso–Martins–Robbiano–Rojo。本文给出它们在这两族上的明确专门化，不能把这些工具全算作新发现。

## 一个独立的路标下界

一个**模** $M$ 是非空真顶点子集，每个外部顶点要么与 $M$ 中全部顶点相邻，要么全不相邻。连通图中，外部顶点到模内各点距离一样，所以外部路标分不开模内点。令 $\rho(M)$ 是在 $M$ 内挑选路标、用诱导图距离截断至 $2$（不连通也取 $2$）来分辨 $M$ 所需的最小数目；单点的 $\rho$ 为 $0$。

::: {.remark #module-bound title="原文推论 7：不交模的度量下界" mathesis="collected:aks2610-twin-free-theta-separation:2:s7"}
在有限简单连通图 $G$ 中，对任意有限列两两不交的非空真模 $M_1,\ldots,M_s$，有 $\dim G\geq\sum_i\rho(M_i)$。原文第 5 节推论 7 重述并证明 Belmonte–Fomin–Golovach–Ramanujan（2016）第 4 节引理 7 中已有的下界。[模下界请求](https://github.com/the-omega-institute/trureturing-requests/issues/43)。
:::

每个真模在连通图中有一个与它所有点相邻的外部点，所以模内不相邻的点距离至多 $2$。任何分辨集都必须在 $M_i$ 内提供至少 $\rho(M_i)$ 个路标。模不相交，数量才能相加。孪生类大小为 $m$ 时，这给出熟悉的 $m-1$ 下界。这是距离下界，不是一般谱等式判别法。
