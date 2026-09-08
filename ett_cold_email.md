Subject: Prospective Postdoc — Causal Inference for Health Preference (Yichao Jin)

Dear Professor Tchetgen Tchetgen,

I am writing to ask whether your group at the University of Pennsylvania is currently considering postdocs working on causal inference for health applications, and whether a candidate with my training would be a good fit.

I recently completed my Ph.D. in Public Policy and Political Economy at UT Dallas (May 2026), with a dissertation that built mixed-logit discrete choice models to estimate how waiting time and institutional trust jointly shape stated vaccination choice in a Wuhan DCE (N = 1,027; 18,486 choice sets). The methodology grew out of a thread I think maps onto your work on semiparametric efficiency theory and causal inference under endogeneity: I built a structural model in which preference heterogeneity and unobserved covariates are jointly estimated, then used the implied heterogeneity distribution to project policy effects.

Three threads of my work seem to connect to your group:

(i) Preference heterogeneity as a structural causal model. The mixed-logit specification decomposes the latent coefficient on waiting time into a Normal distribution with σ = 1.272 and 40.7% positive mass. Treating the latent coefficient as a structural parameter rather than nuisance lets me ask "for whom does waiting time act as a barrier?" --- the same target-trial-style pre-registration problem your group has worked on for treatment regimes.

(ii) Trust interaction under endogeneity. Subgroup MXLs by trust score produced β_wait = -0.184 (high trust, n=446), -0.292 (low trust, n=226), and -0.563 (neutral, n=261). The joint categorical Wald test against high-trust reference (χ²(2) = 13.87, p < 0.001) is significant even after continuous interaction controls (LR = 1.21, p = 0.27), suggesting discrete-group heterogeneity that the linear-interaction model misses --- which I think is exactly the kind of finding that motivates your doubly-robust work.

(iii) BDT framework: a behavioral-digital-twin approach for policy simulation. My working paper, "Empirical-Frontier Regularization for LLM Synthetic Agents" (BDT; targeted at Value in Health), develops an inference-time procedure that anchors LLM-generated choice probabilities to a DCE-estimated empirical frontier (λ = 0.25 blending weight). The bridge between your semiparametric efficiency work and my framework is the question: how should we ground generative models in empirical preference data without losing efficient estimation?

I work daily in R and Python, am comfortable with Stata and MATLAB, and have a strong discipline around reproducible data pipelines. I would be glad to share my CV and research statement on request.

I would be grateful for two minutes of your time: is your group considering postdoc candidates with my profile, and if so, would a candidate with my methodological background be a good fit? I am flexible on start date and would be glad to begin before or at Fall 2026.

Thank you very much for your consideration.

Yichao Jin, Ph.D.
School of Economic, Political and Policy Sciences
The University of Texas at Dallas
Yichao.Jin@UTDallas.edu · https://yichao2022.github.io