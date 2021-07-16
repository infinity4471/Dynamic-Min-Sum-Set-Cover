# Dynamic-Min-Sum-Set-Cover

This repository contains the complete work for my Master Thesis *On the approximability of Dynamic Min-Sum Set Cover*. Browsing this repo you can find:

- The LaTeX source of our original paper + our paper in PDF format: [On the Approximability of Multistage Min Sum Set Cover](https://drops.dagstuhl.de/opus/volltexte/2021/14134/) as submitted on [ICALP 2021](http://easyconferences.eu/icalp2021/).

- The LaTeX source of my Master Thesis + my thesis in PDF format as submitted to receive my Integrated Master's in Electrical and Computer Engineering.

- The beamer source of my Master Thesis presentation + the slides in pdf format.

- The algorithms we developed in our paper implemented in python.

# Description

We investigate the polynomial-time approximability of the dynamic version of Min-Sum Set Cover, a natural and intriguing generalization of the classical List Update problem. In $\DSSC$, we maintain a sequence of permutations `
(\pi^0, \pi^1, \ldots, \pi^T)` on n elements, based on a sequence of requests `R = (R^1, \ldots, R^T)`. We aim to minimize the total cost of updating `\pi^{t-1}` to `\pi^{t}`, quantified by the Kendall tau distance, plus the total cost of covering each request $R^t$ with the current permutation $\pi^t$, quantified by the position of the first element of `R^t` in `\pi^t`. 

Using a reduction from Set Cover, we show that Multistage Min-Sum Set Cover does not admit an `O(1)`-approximation, unless `P=NP`, and that any `o(log n)` (resp. `o(r)`) approximation to  Multistage Min-Sum Set Cover implies a sublogarithmic (resp. `o(r)`) approximation to Set Cover (resp. where each element appears at most r times). Our main technical contribution is to show that Multistage Min-Sum Set Cover can be approximated in polynomial-time within a factor of `O(log^2 n)` in general instances, by randomized rounding, and within a factor of `O(r^2)`, if all requests have cardinality at most r, by deterministic rounding.
