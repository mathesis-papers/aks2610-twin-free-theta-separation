# Turn the whole graph into a recurrence

## Split the patterns into two kinds

Exchange $a\leftrightarrow c$ and $b\leftrightarrow d$, leaving everything else fixed. Doing this twice restores the original pattern, and the exchange commutes with both $L$ and $Q$. Any number pattern is the sum of its average with the exchanged pattern and half their difference. The first part stays fixed and is called symmetric; the second changes sign and is called antisymmetric. Study them separately, then add their dimensions at each common eigenvalue.

An antisymmetric pattern is zero at the terminals and along the long path. It has values $(B,C)$ at $(a,b)$ and $(-B,-C)$ at $(c,d)$. Contributions at the terminals cancel. Write both rules as $M_e=D-eA$, with $e=1$ for $L$ and $e=-1$ for $Q$. The entire antisymmetric part reduces to

$$
\begin{pmatrix}2&-e\\-e&2\end{pmatrix}.
$$

Substituting $(B,C)=(1,1)$ and $(1,-1)$ gives eigenvalues $2-e$ and $2+e$: these are $1,3$, each with one direction. These patterns exist regardless of the long path's length. Repetition depends on whether the symmetric part also has the same eigenvalue.

## The long path remembers only its first two numbers

A symmetric pattern has terminal values $A,D_0$, values $B,C$ on each short path, and long-path values $Y_j$. For eigenvalue $\lambda$, introduce $t=e(2-\lambda)$. Each interior vertex has degree $2$, so the eigenvalue equation becomes

$$
Y_{j+1}=tY_j-Y_{j-1}.
$$

Knowing $Y_0,Y_1$ determines the entire path. An arbitrarily large matrix problem has become two initial numbers plus compatibility at the ends. The short paths and terminals also require

$$
\begin{aligned}
tB&=A+C,&tC&=B+D_0,\\
Y_0&=A,&Y_r&=D_0,\\
Y_1&=(t+e)A-2B,&Y_{r-1}&=(t+e)D_0-2C.
\end{aligned}
$$

The terms $2B,2C$ come from the two short paths. Together with the recurrence, these conditions are both necessary and sufficient: they account for every vertex row of the matrix equation.

## Why modulo six?

At $t=1$, starting from $(Y_0,Y_1)=(A,s)$ gives

$$
A,s,s-A,-A,-s,A-s,A,s,\ldots.
$$

At $t=-1$, the sequence is

$$
A,s,-A-s,A,s,-A-s,\ldots.
$$

The first repeats every $6$ steps and the second every $3$. Endpoint compatibility therefore depends only on the remainder of $r$ modulo $6$. This is the source of the congruence classification.

For $r=6k+4$, $k\geq1$, substituting in the endpoint equations gives the table below. Here dimension counts independent symmetric patterns, rather than landmarks.

| Matrix | Symmetric dimension at $t=1$ | Symmetric dimension at $t=-1$ |
|---|---|---|
| $L$ | $1$ | $1$ |
| $Q$ | $0$ | $0$ |

For example, when $e=1,t=1$, take $A=s=1$, $D_0=-1$, $B=1/2$, $C=-1/2$, and fill the long path using the six-periodic sequence. This pattern is independent of the antisymmetric pattern and has the same eigenvalue $\lambda=1$. The case $t=-1$ contributes another symmetric direction. Thus $1,3$ are at least double for $L$, whereas $Q$ has only its single antisymmetric direction at each value.

## The difficult step: rule out hidden repetitions elsewhere

Finding patterns at $1,3$ does not establish that these are the only repeated eigenvalues. Section 3.2 of the manuscript supplies the exclusion argument. Put

$$
p_0=1,\quad p_1=t,\quad p_{n+1}=tp_n-p_{n-1}.
$$

The recurrence gives two identities:

$$
\begin{aligned}
Y_r&=p_{r-1}Y_1-p_{r-2}Y_0,\\
p_n^2+p_{n+1}^2-tp_np_{n+1}&=1.
\end{aligned}
$$

The second expression is unchanged from $n$ to $n+1$ and starts at $1$. If $q=t^2-1\ne0$, the short-path equations give $qB=tA+D_0$ and $qC=A+tD_0$, so the endpoint pair determines the entire pattern. With $P=p_{r-1}(t)$, $R=p_{r-2}(t)$, the pair must satisfy

$$
(q+2P)D_0=\bigl(P((t+e)q-2t)-Rq\bigr)A.
$$

If this is a nonzero linear condition, the allowed endpoint pairs lie on a line through the origin. The symmetric eigenspace then has dimension at most one. The danger is that both coefficients vanish. Substitution of that assumption into the identity forces

$$
(t-2e)(t^2-1)(t^2+2et-1)=0.
$$

The case $t^2=1$ was handled separately. At $t=2e$, the recurrence gives $P=e^{r-1}r$, incompatible with the required value $-3/2$. Finally, $t^2+2et-1=0$ would also require $R=e$. A rational polynomial vanishing at one of these irrational conjugate roots vanishes at the other. Thus $p_{r-2}(T)=e$ would hold at $T=-e(1+\sqrt2)$. But $|T|>2$: recurrence magnitudes grow strictly from $1,|T|$, so $|p_{r-2}(T)|>1$ for $r\geq3$, a contradiction.

This excludes all other repetitions: the symmetric part has dimension at most one, and the antisymmetric part is nonzero only at $1,3$. Since the matrices are real symmetric, eigenspace dimensions equal algebraic multiplicities.

::: {.remark #theta-main title="Manuscript Theorem 1: the precise spectrum of the main family" mathesis="collected:aks2610-twin-free-theta-separation:2:s1"}
Sections 1–3 prove the following. For every integer $k\geq1$, put $r=6k+4$, $G=\Theta_{3,3,r}$. Then $G$ is connected and twin-free, $|V(G)|=r+5$, $\dim G=\operatorname{mm}_L G=2$ and $\operatorname{mm}_Q G=1$. The only repeated eigenvalues of $L$ are $1,3$, each double; all its other eigenvalues are simple. Every eigenvalue of $Q$ is simple. This is the complete manuscript conclusion. Neither the geometric Lean theorem above nor the existential Lean theorem later states this complete spectral list. [Formalization request for the precise refinement](https://github.com/the-omega-institute/trureturing-requests/issues/39).
:::

::: {.remark #explicit-family title="Manuscript Corollary 2: an explicit infinite family" mathesis="collected:aks2610-twin-free-theta-separation:2:s2"}
The graphs $G_k=\Theta_{3,3,6k+4}$, $k\geq1$, in Corollary 2 are pairwise nonisomorphic, and each satisfies exactly one equality. It remains only to observe that their orders $6k+9$ strictly increase with $k$. Specifying these graphs is more concrete than the existential declaration cited later. This refinement shares the [main-family request](https://github.com/the-omega-institute/trureturing-requests/issues/39); it does not request another proof of the existing existential theorem.
:::
