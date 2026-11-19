# 两个路标与两种图的频率

想象一张步行地图：交叉口是点，道路是边，每条边走一步。你只知道到两个指定路标各有几步，能否确定自己的位置？另一个看似无关的问题是：给每个点写一个实数，让相邻点按固定规则交换数值，有多少种彼此独立的数值图案具有同一缩放率？本文把这两个问题放在同一族地图上比较，发现它们可以在一种规则下恰好相等，在另一种规则下不相等。

本文依据 Haobo Ma、Wenlin Zhang 的论文 [A twin-free answer to Alfuraidan–Khan–Sauras-Altuzarra, arXiv:2610.26875v1, Section 9, Problem 30 (p. 27): a spectral extension of Knor–Sedlar–Škrekovski (2022)](https://doi.org/10.5281/zenodo.24212419)第 2 版。下文的原文定理和章节编号均指这一版本。

本书讲解 Haobo Ma 与 Wenlin Zhang 的公开论文第 2 版，原题为 *A twin-free answer to Alfuraidan–Khan–Sauras-Altuzarra, arXiv:2610.26875v1, Section 9, Problem 30 (p. 27): a spectral extension of Knor–Sedlar–Škrekovski (2022)*。作者依次为 Haobo Ma（Chrono AI，新加坡）与 Wenlin Zhang（新加坡国立大学及 Chrono AI，新加坡）。原文与讲解采用 CC BY 4.0。原文日期为 2026 年 11 月 5 日，公开第 2 版发布于 11 月 14 日。

## 先从一条路开始

沿直线排列的五个点，可以用端点作唯一的路标：距离依次是 $0,1,2,3,4$，每个人的位置都有不同的号码。但在分叉路口，一个路标可能分不清两个方向上同样远的点。选择一组路标，使每个点的距离清单都不同，称为**分辨集**；所需路标的最小数目，称为图的**度量维数**，记为 $\dim G$。这里的“维数”数的是路标，并非地图需要几维空间才能画出来。

论文使用的地图有两个端点 $u,v$，两者之间有三条内部互不相交的路。两条各长 $3$ 条边，第三条长 $r$ 条边。这就是 $\Theta_{3,3,r}$。写下

$$
\begin{gathered}
u-a-b-v,\qquad u-c-d-v,\\
u=y_0-y_1-\cdots-y_r=v.
\end{gathered}
$$

端点只数一次，所以共有 $2+2+2+(r-1)=r+5$ 个点。下标表示**边数**，不是内部点数；混淆这个约定会把同余条件错移一位。

现在取 $r=10$。这张地图有 $15$ 个点。把路标放在 $a$ 和 $y_1$，两个路标就足以分清所有点。[下一章](01-landmarks.md)列出全部距离对，你可以亲自核对。

## 两种数值规则

令 $x_w$ 是点 $w$ 上的实数。两个规则分别给出每个点 $v$ 的新数：

$$
\begin{aligned}
(Lx)_v&=\deg(v)x_v-\sum_{w\sim v}x_w,\\
(Qx)_v&=\deg(v)x_v+\sum_{w\sim v}x_w.
\end{aligned}
$$

$\deg(v)$ 是连到 $v$ 的边数，$w\sim v$ 表示相邻。$L=D-A$ 叫拉普拉斯矩阵，$Q=D+A$ 叫无符号拉普拉斯矩阵；$D$ 记录度数，$A$ 记录邻接关系。如果某个非零数值图案 $x$ 经过规则后变成 $\lambda x$，就称 $x$ 为特征向量、$\lambda$ 为特征值。可以把 $\lambda$ 理解为缩放率，“频率”只是帮助直觉的说法。

同一特征值有多少个独立图案，称为它的重数。例如单条边的两个端点写 $(1,1)$ 时，$L$ 把它变为 $(0,0)$；写 $(1,-1)$ 时，$L$ 把它变为 $(2,-2)$。这里两个特征值 $0,2$ 各只有一个独立方向，最大重数为 $1$。写 $\operatorname{mm}_L G$ 和 $\operatorname{mm}_Q G$，指的是在**所有特征值中取最大的重数**，不是“最大特征值的重数”。

## 为什么排除“孪生点”？

两个不同点 $p,q$ 若满足 $N(p)\setminus\{q\}=N(q)\setminus\{p\}$，便是孪生点：忽略彼此后，邻居完全相同。它们可以相邻，也可以不相邻。孪生点会同时制造距离难题与重复的数值图案，使某些相等关系较容易出现。

Alfuraidan、Khan 与 Sauras-Altuzarra 在 arXiv:2610.26875v1 第 9 节第 30 题（第 27 页）问：有没有无限多个互不同构、连通且**没有孪生点**的图，使

$$
\operatorname{mm}_L G=\dim G,\qquad
\operatorname{mm}_Q G=\dim G
$$

这两个等式恰好只有一个成立？“互不同构”表示不能只靠重新命名顶点把两个图变成同一张地图。

论文的主要例子给出肯定回答：取任意整数 $k\geq1$，令 $r=6k+4$。原文证明

$$
\begin{gathered}
\dim\Theta_{3,3,r}=\operatorname{mm}_L\Theta_{3,3,r}=2,\\
\operatorname{mm}_Q\Theta_{3,3,r}=1.
\end{gathered}
$$

两条短路可以互换，但它们的内部点不是孪生点。这种“整个部件对称、单个点并不孪生”的区别，是故事的核心。谱的重复来自两个不同对称类型的图案在同一特征值相遇。[谱的章节](02-recurrence.md)解释它们为什么在 $L$ 中相遇，却在 $Q$ 中错开。

## 怎样阅读

先看[路标与距离证书](01-landmarks.md)，再看[对称与递推](02-recurrence.md)。[完整分类与另外两种构造](03-classification.md)交代小参数例外、此前文献及结论边界。[来源与精确形式化范围](04-sources.md)区分原文的书面论证与 Lean 声明真正说出的内容。

下面的中英文讨论班讲稿沿着同一条故事线：路标、对称、递推、分类与证据范围。

::: {.slides src="seminar"}
学术报告：两个路标为何只与一种谱重数相等，附讲者备注。
:::

下面的短片介绍问题的来由，以及论证背后的关键想法。

::: {.film src="001-landmarks"}
通过旁白与图示，介绍问题和它背后的数学机制。
:::
