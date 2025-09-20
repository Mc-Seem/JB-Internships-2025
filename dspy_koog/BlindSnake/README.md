## Blind Snake Exploration

The strategy that maximizes the winrate in our version of the snake game is:

>Each step, flip an unbiased coin:
>- If it lands on heads - go up
>- If it lands on tails - right

The chance that a field of size $S$ will have an unvisited cell in that case amounts to: $6.3 \cdot 10^{-16} S$ for large values of $S$. 
With random walks, the winrate in our game is basically 100%. I shall hereby prove it.

### Proof

- We can present the state of the game as a Markov chain
- The one-step transition matrix $T$ of size $S \times S$ represents chances of all possible transitions between cells
	- From each cell, there are only two options, where to go: $up$ and $right$, with equal $0.5$ chances
	- Similarly, each cell can be visited from exactly two cells, with equal chances $0.5$
	- The matrix $T$ is thus double-stochastic (the sum of all elements in each row and each column are $1$)
- A uniform distribution $\pi(i) = \frac{1}{S}$ then satisfies $\pi T = \pi$
- The snake's spawn is also uniform (the probability of the snake spawning in any cell is $1/S = \pi$)
- For a time-homogeneous chain that starts from a stationary distribution $\pi$, the marginal at any time is stationary
  - So for every $t$, $Pr(X_i = \textrm{some cell i}) = \frac{1}{S}$
- Therefore, the expected number of visits to an arbitrary cell in the first $N$ steps is $\frac{N}{S}$
- For $N = 35S$ (the maximum number of steps the snake can take before losing) this equals $35$

#### Loss probability

Let us estimate the number of empty cells after first $35S$ steps.

$$
\begin{array}{}
\mathbb{E}[\textrm{empty}] = S(1 - \frac{1}{S})^{35} \approx Se^{-35}\;| \;\textrm{ at large values of } S
\\
\\
\mathbb{E}[\textrm{empty}] \approx Se^{-35} \approx 6.3 \cdot 10^{-16}S
\end{array}
$$

This number is astronomically small and it is safe to assume the strategy maximizes the winrate.
