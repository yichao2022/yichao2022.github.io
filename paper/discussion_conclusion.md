# 5 Discussion

## 5.1 Principal Findings

This study evaluated whether LLM-based synthetic agents can be behaviorally calibrated to produce policy-relevant predictions that respect empirically grounded preference structures. Three principal findings emerged.

First, unconstrained LLMs exhibit systematic violations of established behavioral regularities. Across all models tested, waiting-time monotonicity was violated in 55–70% of pairwise comparisons, and rank-order agreement with an empirical DCE reference was near zero or negative. These violations were not random noise but followed a consistent pattern: LLMs systematically underweighted waiting time relative to other attributes, producing preference orderings that diverged from observed choice behavior.

Second, empirical-frontier regularization (EFR) substantially reduced these inconsistencies. The Static-BDT Anchor reduced monotonicity violation rates from 62.5% to 4.2% and improved Spearman rank correlation from −0.024 to 0.952. Policy Ranking Consistency (PRC) increased by 32–47 percentage points across three language models, with the best-performing model reaching 86.7% agreement with the DCE-derived policy ordering. These improvements were sustained under out-of-design policy narratives: BDT maintained perfect waiting-time monotonicity across 20 paired scenarios where unconstrained LLMs showed near-zero rank alignment.

Third, the choice of regularization anchor matters. The Static-BDT Anchor consistently outperformed the Dynamic-BDT and Distribution-Matching approaches, particularly when the DCE sample was small. This suggests that anchoring to a direct empirical estimate of the choice function provides stronger behavioral constraints than distribution-level regularization or dynamically weighted alternatives, at least within the class of preference structures studied here.

## 5.2 Methodological Contributions

This work makes three methodological contributions.

First, we introduce a general framework for embedding empirical choice constraints into LLM-based policy simulation. The framework treats behavioral anomalies as optimization targets rather than descriptive observations, enabling LLM outputs to be projected onto a preference-consistent subspace without modifying the underlying model architecture. This is distinct from fine-tuning approaches, which require task-specific training data and access to model weights, and from prompt-based mitigation strategies, which show limited effectiveness for persistent structural violations.

Second, we demonstrate that DCE-derived empirical frontiers provide a principled source of behavioral constraints. DCE methods are already widely used in health economics and biomedical informatics to quantify patient and provider preferences. The proposed framework leverages existing DCE infrastructure without requiring new data collection, making it feasible for applications where empirical choice data already exist.

Third, we propose and validate the out-of-design evaluation framework as a stress test for LLM-based policy simulation. Unlike held-out validation within a structured attribute space, out-of-design scenarios require the LLM to process unstructured textual descriptions while maintaining behavioral consistency—a task that unconstrained models systematically fail. This evaluation paradigm may be useful for other applications where LLM-generated predictions must align with known behavioral constraints under distributional shift.

## 5.3 Implications for Biomedical Informatics

LLM-based synthetic agents have been proposed as tools for policy simulation, patient preference modeling, and clinical decision support. This study identifies a practical barrier to such applications: without empirical calibration, LLM-generated preference predictions can be systematically misleading, with error patterns that are not detectable from standard evaluation metrics.

For biomedical informatics, the findings suggest two implications. First, the integration of DCE-generated behavioral data into LLM pipelines offers a practical path toward more reliable policy simulations. Systems that maintain populations as LLM-based synthetic agents can incorporate empirical constraints as a post-hoc regularization layer, analogous to how clinical prediction models are calibrated against observed outcomes before deployment. Second, the out-of-design evaluation framework introduced here may serve as a template for stress-testing LLM-based decision support tools before they are applied to novel policy scenarios. The finding that unconstrained LLMs systematically reverse preference orderings under rich textual narratives highlights the need for behavioral validation protocols in LLM-enabled health applications.

## 5.4 Limitations and Future Directions

Several limitations should be acknowledged.

First, the empirical behavioral reference is a DCE-based model of stated preferences, not observed choice behavior. While DCE is a well-established method for eliciting preferences in health contexts, stated preferences may diverge from revealed preferences in real-world settings. External validation against observed policy outcomes remains necessary to establish real-world predictive validity.

Second, the current implementation evaluates a single behavioral regularity—waiting-time monotonicity—within a specific health policy domain (vaccination access). The extent to which EFR generalizes to other preference structures (e.g., nonlinear utility functions, attribute interactions, choice under uncertainty) and other policy domains remains to be tested.

Third, the out-of-design evaluation, while designed to test behavioral consistency under distributional shift, is limited to 20 paired policy scenarios. These scenarios were constructed to challenge the models rather than to represent a random sample of plausible policy descriptions, and the results should be interpreted as descriptive robustness measures rather than population-level estimates.

Fourth, the Static-BDT Anchor depends on having DCE data of sufficient quality and sample size. When the DCE sample is very small, the empirical behavioral reference may itself be noisy, and the regularization may propagate rather than correct measurement error. Appendix~\ref{app:data_scaling} examines this sensitivity.

Future work should extend the framework to multi-attribute non-linearities, investigate whether the regularization approach can be integrated with actively learning models that update empirical frontiers as new data become available, and validate the approach against real-world policy outcomes where observed choice data exist.

# 6 Conclusion

LLM-based synthetic agents offer a scalable approach to policy simulation, but their usefulness depends on whether their predictions respect empirically grounded behavioral constraints. This study demonstrates that unconstrained LLMs produce systematic violations of established preference regularities, and that empirical-frontier regularization can substantially reduce these inconsistencies. By anchoring LLM predictions to a DCE-derived choice function, the proposed framework preserves behavioral consistency across both structured attribute combinations and rich out-of-design policy narratives, without requiring model re-training or architecture modifications. While limitations remain—particularly the need for external validation against observed outcomes and extension to broader preference structures—these findings suggest that empirical regularization is a viable strategy for making LLM-based policy simulations behaviorally meaningful.
