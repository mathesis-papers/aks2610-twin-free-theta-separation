# 精确结论、来源与贡献入口

## 存在性与完整分类是不同的陈述

::: {.theorem #infinite-separation title="无限个无孪生点的分离例子" lean="D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaSeparation.result" mathesis="collected:aks2610-twin-free-theta-separation:2:s2"}
存在阶数序列 $(n_i)_{i\in\mathbb N}$ 及顶点集为 $\{0,\ldots,n_i-1\}$ 的简单图 $G_i$，使每个 $G_i$ 连通且无孪生点，并且

$$
\begin{gathered}\bigl(\operatorname{mm}_L G_i=\dim G_i\\\text{且}\quad\operatorname{mm}_Q G_i\ne\dim G_i\bigr)\\\text{或}\\\bigl(\operatorname{mm}_Q G_i=\dim G_i\\\text{且}\quad\operatorname{mm}_L G_i\ne\dim G_i\bigr).\end{gathered}
$$

此外，对任意 $i\ne j$，不存在 $G_i$ 到 $G_j$ 的图同构。
:::

这与公开声明 `TwinFreeThetaSeparation.result` 展开的 `claim` 相同。它是原文推论 2 的存在性后果，并非推论 2 对明确指定的 $G_k$ 所作断言的逐字形式化。证明选取 $n_i=6(i+1)+9$、$G_i=\Theta_{3,3,6(i+1)+4}$，即 $k=i+1\geq1$，并选择上式的第一个分支。但**结论本身**没有指定这些见证、方向、确切最大重数或重复特征值清单。不能把证明里使用的见证误当成公开结论已经列出的全部性质。

几何声明 `theta_metric_certificates` 则对每个自然数 $k\geq1$ 明确证明连通、无孪生点与度量维数 $2$。原文完整的谱分类仍需另行形式化。

## 应怎样读证据

| 内容 | 这里的依据与范围 |
|---|---|
| $r=6k+4$ 的连通、无孪生点、度量维数 $2$ | 几何 Lean 声明，要求 $k\geq1$ |
| 无限个互不同构、恰好一个等式成立的图存在 | 存在性 Lean 声明，不指定谱清单 |
| 主族只有 $1,3$ 重复以及全长度分类 | 原文书面证明；有出处的注记及共享请求 |
| $Q$ 的特征值 $2$、挂路径双向例子、模下界 | 原文证明与所引既有文献；分别登记请求 |
| 原文报告的 $2\leq r\leq40$ 精确计算 | 有限范围的佐证，不是全参数证明 |

有限计算用于说明书面论证。适用于所有参数的证明来自递推式和端点方程；已有 Lean 结果的精确范围见上表。

## 哪些问题已经回答，哪些没有？

原问题只要求有一个分离方向的无限族，所以主要 theta 族已经肯定回答第 30 题；挂路径推论进一步给出两个方向。完整 theta 分类回答第 29 题在 $\Theta_{3,3,r}$ 子族内的同余问题，没有分类所有三条路径长度。

这里没有分类所有连通图的等式条件（第 28 题），没有改进按阶数计数的指数下界（第 31 题），也没有给出一般分割的谱等式判别法（第 32 题）。模下界与交换短路的等分划分例子是局部贡献。每个根接一条路径，也不是第 33 题所要求的每根多条分枝。尤其，“这个 theta 子族没有无符号方向的独有例子”不等于“所有无孪生点图都没有”；挂路径的第二族恰好展示相反方向。

## 原文与此前工作

原论文第 2 版、作者及许可见 [Mathesis 公开记录](https://mathesis-omega-research.apps.chrono-ai.fun/papers/aks2610-twin-free-theta-separation?version=2)。固定版本的 [Lean 存在性源码](https://github.com/the-omega-institute/trureturing/blob/d9bb8a406783c5222849b798f3c2ab738f653d75/D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaSeparation.lean)与[几何源码](https://github.com/the-omega-institute/trureturing/blob/d9bb8a406783c5222849b798f3c2ab738f653d75/D5/S3/Combinatorics/SpectralGraph/TwinFreeThetaStructure.lean)便于核对原文采用的公开形式化范围。

| 文献 | 本文采用的内容 |
|---|---|
| Alfuraidan–Khan–Sauras-Altuzarra, *Metric dimension and maximum eigenvalue multiplicity of graph Laplacians*, [arXiv:2610.26875v1](https://arxiv.org/abs/2610.26875v1) | 第 9 节第 30 题；表 2 的 $r=2$ 图；挂路径构造的底图 |
| Knor–Sedlar–Škrekovski, *Remarks on the vertex and the edge metric dimension of 2-connected graphs* (2022), [10.3390/math10142411](https://doi.org/10.3390/math10142411) | arXiv 版定理 8、14 的度量分类；本文新内容不是首次证明该度量分类 |
| Benakli–Froitzheim–Martinez (2025), [arXiv:2510.12100v1](https://arxiv.org/abs/2510.12100v1), 定理 4.4 | 后来的另一种度量证明；其参数数内部顶点 |
| Bahmani–Kiani, [arXiv:1512.08265v5](https://arxiv.org/abs/1512.08265v5), 推论 16 | 特定特征值 $1,3$ 的周期性；不负责排除别处重根 |
| Liu–Lu, [arXiv:1407.5255v2](https://arxiv.org/abs/1407.5255v2), 命题 2.6 | 较早的 theta 特征多项式公式 |
| A. Paone–M. Paone, *Line-graph inertia of roses and generalized theta graphs*, v1.0 (2026), [10.5281/zenodo.21744051](https://doi.org/10.5281/zenodo.21744051), 推论 8.1 | 无符号特征值 $2$ 的既有公式 |
| Jannesari (2023), [10.5666/KMJ.2022.63.1.123](https://doi.org/10.5666/KMJ.2022.63.1.123), 定理 2.2 | 挂一片叶子的度量准则 |
| Feng–Wang, [arXiv:1211.1432v1](https://arxiv.org/abs/1211.1432v1), 命题 2.10 | 直径二底图的长路径度量工具 |
| Cardoso–Martins–Robbiano–Rojo (2013), [10.13001/1081-3810.1681](https://doi.org/10.13001/1081-3810.1681), 定理 2.1 | 根积谱的分块公式 |
| Belmonte–Fomin–Golovach–Ramanujan, [arXiv:1602.02610v1](https://arxiv.org/abs/1602.02610v1), 第 4 节引理 7 | 模的度量下界 |

## 沿同一个共享请求参与

可分别参与[主族精确谱](https://github.com/the-omega-institute/trureturing-requests/issues/39)、[全长度分类](https://github.com/the-omega-institute/trureturing-requests/issues/40)、[特征值二](https://github.com/the-omega-institute/trureturing-requests/issues/41)、[挂路径构造](https://github.com/the-omega-institute/trureturing-requests/issues/42)或[模下界](https://github.com/the-omega-institute/trureturing-requests/issues/43)。请求保留原作者、此前工作、精确版本与适用范围。先在对应请求说明具体要做的部分，再按[上游贡献规范](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)，从贡献者自己的 fork 向上游 `dev` 提交聚焦的 PR。形式化合入后仍需逐条比较声明；issue 关闭或 CI 通过不自动覆盖整篇论文，也不产生平台积分或收据。
