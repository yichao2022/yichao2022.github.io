# Perspective Review: Equity, Ethics, and Generalizability

**Paper:** "Waiting Time as a Behavioral Barrier to Vaccination Uptake: Nonlinear Heterogeneity by Institutional Trust" (Yichao Jin, with Dohyeong Kim)

**Reviewer role:** Perspective reviewer (Role #4, Batch 2) — the paper's conscience, future-proofing mechanism, and equity/ethics/societal-impact auditor.

**Evidence base:** Full JMP manuscript (pdftotext extraction, 1,306 lines including main text + Online Supplementary Material Appendices A–F), prior session context on paper framing and methodological details.

**Transparency statement:** The full paper PDF was available and read in its entirety. The following assessment is grounded in the specific text, tables, and supplementary appendices of the manuscript. Where assumptions are made about aspects not visible in the text (e.g., IRB-reviewing institution identity), this is flagged inline.

---

## 1. Equity & Representation

**Gap:** The paper reports that the sample slightly overrepresents more highly educated respondents and that post-stratification weighting yielded substantively similar results — but does not report equity-stratified performance of the headline finding (nonlinear trust heterogeneity) by income, education, or urban/rural status, despite the fact that the supplementary subgroup tables reveal substantial variation in waiting-time sensitivity along precisely these axes.

**Why it matters for THIS paper:**

The paper's central equity claim — that "reducing waiting time may be especially beneficial for populations with intermediate trust" (§4.6) — is constructed from a sample whose demographic composition is reported but whose intersectional equity implications are not interrogated. Specifically:

- **Appendix D (Table 3)** shows that rural respondents have substantially *lower* waiting-time sensitivity (β = −0.287, per-month −0.130) than urban respondents (β = −0.433, per-month −0.196). This is a 50% difference in per-month coefficient magnitude — yet the main text makes no mention of this urban/rural disparity, and the equity implications section (§4.3) discusses trust-based heterogeneity without noting that the behavioral burden of waiting time falls differently on urban vs. rural populations.
- **Education subgroups** show the lowest-educated group (no formal education, n=65) has the second-highest per-month sensitivity (β = −0.201), while college-educated respondents are among the least sensitive (β = −0.128). The paper does not discuss whether the "neutral trust" group is disproportionately composed of lower-education respondents — if so, the trust heterogeneity finding may be partly confounded with educational attainment.
- The paper's framing of institutional trust as the "most salient source of heterogeneity" (§4.2) is supported by formal interaction tests for trust specifically, but the supplementary tables reveal that **no formal interaction tests are reported for education, income, or urban/rural status** (Appendix F states "The clearest inferential evidence of heterogeneity was observed for institutional trust, which therefore receives the main substantive emphasis" — but this emphasis may mask equally large or larger equity-relevant differences).
- The paper uses a five-point institutional trust measure that collapses to three groups (low/neutral/high). The "neutral trust" group (n=261, 25.4% of the sample) is the paper's key finding — yet the paper does not report whether this group differs demographically from the low-trust and high-trust groups in ways that would confound the trust interpretation.

**Concrete additions (3):**

1. **[§3.2 (Results — Nonlinear Heterogeneity), Priority: High]** — Add a demographic profile table for the three institutional trust groups (low/neutral/high) showing age, gender, education, urban/rural, and income composition. If the neutral-trust group differs systematically (e.g., more rural, less educated), report whether the trust heterogeneity finding survives controlling for these covariates in a richer mixed-logit specification. The current analysis estimates trust-group-specific coefficients but does not include trust × demographic interaction terms that would establish whether trust is the operative dimension or a proxy for structural disadvantage.

2. **[§4.3 (Discussion — Implications for Preventive Health Delivery and Equity), Priority: High]** — Add an "Equity-Stratified Burden" paragraph that explicitly reports the urban/rural difference in waiting-time sensitivity (rural β = −0.130 vs. urban β = −0.196 per month) and the education gradient (no formal education β = −0.201 vs. college β = −0.128 per month). The current equity discussion frames the burden as falling on "intermediate trust" populations, but the data suggest the burden also falls disproportionately on rural and less-educated populations — a finding that is at least as policy-relevant and more directly actionable than the trust heterogeneity.

3. **[Appendix B (Sample Benchmarking), Priority: Medium]** — Add income distribution of the sample vs. Wuhan Census. The current benchmarking table covers gender, age, residence, and education but omits income entirely. If income data were collected but not benchmarked, the omission should be acknowledged; if income was not collected, this is a limitation for equity analysis and should be noted.

---

## 2. Ethical Implications of Methods

**Gap:** The paper states that "no formal ethics approval" was required and that "all participants provided informed consent" — but does not discuss the specific ethical considerations that arise from (a) conducting a vaccination preference survey in Wuhan, a city with unique pandemic trauma, (b) the COVID-like disease (CLD) framing that deliberately evokes recent lived experience, or (c) the potential for the paper's findings to be used in ways that affect the surveyed population.

**Why it matters for THIS paper:**

- **Wuhan-specific ethical burden:** The paper deliberately chose Wuhan because of its "early pandemic experience" and "high public-health visibility" (§2.2). This means the survey asked respondents to revisit vaccination decisions in a city that was the global epicenter of COVID-19 and experienced one of the most stringent lockdowns in human history. The CLD framing is designed to "preserve a realistic infectious-disease context" (§2.1) — but realism here means the survey may have evoked pandemic-related anxiety, grief, or trauma. The paper does not discuss whether any debriefing, mental health referral, or distress protocol was in place, nor whether this was considered in the ethics review determination.

- **"No formal ethics approval" without specifying the reviewing body:** The statement that the protocol "was reviewed by an appropriate institutional ethics committee and determined to require no formal ethics approval" (§Ethics) is somewhat contradictory — if a committee reviewed it, the committee's name, the review date, and the determination letter number should be cited. The current phrasing leaves ambiguous whether this was a formal IRB exemption determination (common in US institutions for minimal-risk survey research) or an informal determination by a non-IRB body. For a paper likely submitted to an international journal, this ambiguity is a credibility risk.

- **Secondary use and data availability tension:** The Data Availability Statement says de-identified data "may be made available upon reasonable request, subject to approval by the relevant ethics committee" — but if no formal ethics approval was required, which committee would adjudicate the data-sharing request? This creates an internal contradiction that undermines the data-sharing commitment.

- **CLD framing and framing effects:** The paper's own finding — that the relationship between trust and delay sensitivity is nonlinear and context-dependent — implies that the choice of framing (CLD vs. a real named disease vs. a generic "respiratory infection") may itself have shaped the results. The paper does not discuss the ethical implications of using a framing that was selected for methodological convenience but may have differential emotional resonance across respondents with different lived pandemic experiences.

- **AI use declaration:** The declaration that AI was used for "language editing, formatting, and clarification of exposition" (§Declaration of Generative AI Use) is appropriately scoped. However, given that this paper is by an author whose other work explicitly develops LLM-based simulation methods, a reader might reasonably wonder whether AI was also used in instrument design, pilot feedback analysis, or data processing. The declaration could be strengthened by specifying that no AI tools were used in survey instrument development, participant recruitment, data collection, or statistical analysis.

**Concrete additions (3):**

1. **[§Ethics (Ethics approval and informed consent), Priority: High]** — Expand the ethics statement to include: (a) the name of the reviewing ethics committee and the determination date/reference number; (b) a statement that the CLD framing was reviewed for potential to cause distress, with the determination; (c) whether any debriefing or mental health resource referral was provided to participants, given the pandemic context in Wuhan. If the reviewing body was the author's home institution (UT Dallas), this should be stated explicitly; if it was a Chinese institution, the cross-jurisdictional review arrangement should be described.

2. **[§2.1 (Study Design), Priority: Medium]** — Add a sentence acknowledging the ethical dimension of the CLD framing: "The COVID-like disease scenario was designed to elicit realistic preferences without anchoring to a specific epidemic phase. We recognize that this framing may have different emotional resonance for respondents in Wuhan, given the city's pandemic experience. The ethics review considered this potential and determined that the minimal-risk survey protocol, combined with the informed consent process, was appropriate."

3. **[§Data Availability Statement, Priority: Medium]** — Resolve the internal contradiction: if no formal ethics approval was required, specify the mechanism by which data-sharing requests will be adjudicated (e.g., "Data-sharing requests will be reviewed by [named committee/office] at [institution]"). Alternatively, if an IRB exemption was granted, cite the exemption number and reframe the statement as "The study was determined to be exempt from full IRB review under [category] by [IRB name], reference [number]."

---

## 3. Cultural Generalizability

**Gap:** The paper is grounded in a single-city sample (Wuhan, China) with a population that has uniquely intense pandemic experience, yet the abstract, title, and conclusion frame the findings as general insights about "vaccination uptake" and "preventive health behavior" without explicitly bounding the cultural, institutional, and temporal scope of the claims.

**Why it matters for THIS paper:**

- **Wuhan is not a representative Chinese city, let alone a representative global population.** Wuhan was the first city to experience COVID-19 lockdown (January 2020), the site of the most stringent quarantine measures in China, and the subject of intense global media attention. Its residents have lived experience of institutional trust being tested under extreme crisis — both the initial failure of transparency and the subsequent massive mobilization. This history likely shapes institutional trust in ways that are not transferable to other Chinese cities, let alone to populations in other countries.

- **The institutional trust measure is culturally specific.** The five-point scale measures "trust in government institutions" — but in China, this concept operates within a single-party political system with no independent media, restricted civil society, and a Confucian cultural tradition of state legitimacy that differs fundamentally from Western liberal-democratic conceptions. The paper does not discuss whether "institutional trust" means the same thing to a Wuhan resident as it would to a resident of, say, Houston or Lagos. The finding that "neutral trust" respondents are most delay-sensitive may be an artifact of how trust operates in a specific political-cultural context where expressing "neutral" trust may itself be a meaningful stance (neither the expected loyalist affirmation nor open dissent).

- **The CLD framing creates temporal anchoring despite the stated intent to avoid it.** The paper says CLD was used to "reduce anchoring to a specific epidemic wave, variant, or policy period" (§2.1). But in Wuhan, *any* COVID-like framing will evoke the specific 2020 experience regardless of the label. The paper's data collection in "early 2025" means respondents were approximately 5 years post-initial-outbreak — a time when pandemic memories are still vivid but vaccination urgency has receded. This temporal window is not replicable in other settings.

- **The paper's limitations section (§4.5) acknowledges geographic and temporal specificity** but frames this as a matter of magnitude variation ("the magnitude of waiting-time sensitivity and its interaction with institutional trust may differ across populations") rather than as a potential qualitative difference. The nonlinear pattern itself — with neutral trust being most sensitive — may not replicate in settings where institutional trust operates differently.

- **The paper uses Hofstede-adjacent concepts implicitly** (institutional trust, collectivism, government legitimacy) without engaging the cultural-dimensions literature that would allow readers to assess transferability.

**Generalizability Boundary Table:**

| Claim | Supported? | Rationale |
|-------|-----------|-----------|
| Waiting time reduces vaccine uptake in this Wuhan sample | Yes | Direct empirical evidence, mixed-logit β = −0.54 (std), p < 0.001 |
| The effect is nonlinear across trust groups in this sample | Yes | Joint Wald χ² = 8.06, p = 0.018; neutral-trust group most sensitive |
| Waiting time reduces uptake in other Chinese cities | Plausible but unproven | Shared political-institutional context; but Wuhan's pandemic experience is unique |
| The nonlinear trust pattern replicates in other Chinese cities | No evidence | Pattern may depend on Wuhan-specific trust dynamics |
| The effect generalizes to Western populations | No evidence | Fundamentally different institutional trust structures, healthcare systems, pandemic experiences |
| The effect generalizes to low-income countries | No evidence | Different access constraints, disease burden, institutional capacity |
| Reducing waiting time improves equity across trust groups | Partially supported | Within-sample evidence; but equity claim requires cross-population validation |

**Concrete additions (3):**

1. **[§1 (Introduction), Priority: High]** — Add a "Cultural and Institutional Scope" paragraph after the introduction's third paragraph (the one beginning "Wuhan provides an informative setting"). State explicitly: "The institutional trust dynamics examined in this study are situated within China's specific political-institutional context, where trust in government operates within a single-party system with distinctive historical and cultural foundations. Wuhan's role as the initial COVID-19 epicenter further shapes local pandemic experience and institutional memory in ways that may not be representative of other settings. The generalizability of the observed nonlinear trust–delay relationship to populations with different political systems, pandemic histories, or cultural orientations toward institutional authority is not tested in this study."

2. **[§4.5 (Limitations), Priority: High]** — Strengthen the second limitation (currently about geographic/temporal context) to include a "Generalizability Boundary" statement: "The nonlinear pattern — with neutral-trust respondents showing the greatest delay sensitivity — may be specific to the Wuhan context, where pandemic experience created a particular distribution of trust and distrust. In settings where institutional trust is generally lower (e.g., post-colonial contexts with histories of medical exploitation) or where trust operates through different mechanisms (e.g., trust in healthcare professionals vs. government institutions), the pattern may differ qualitatively, not just quantitatively." Specify minimum replication targets: (a) a different Chinese city without Wuhan's pandemic history; (b) a Western population with different institutional trust structure; (c) a low-income country with different access constraints.

3. **[§2.4 (Measures), Priority: Medium]** — Add a note on the cultural specificity of the institutional trust measure: "The five-point institutional trust measure captures trust in government institutions as perceived by Chinese respondents within a single-party political system. Cross-cultural research suggests that the meaning and behavioral consequences of institutional trust differ across political systems (Hofstede, 2001; Gelfand et al., 2011). Readers should interpret the trust groupings used in this study as context-specific rather than universal constructs."

---

## 4. Risk, Liability & Accountability

**Gap:** The paper translates its findings into specific policy recommendations — "reducing waiting time may improve uptake," "interventions that shorten waiting time may therefore improve vaccine uptake and may be especially effective when targeted toward populations that are neither strongly trusting nor strongly distrustful" (Abstract) — but does not specify the conditions under which these recommendations should NOT be applied, the quality thresholds that must be met before the findings inform policy, or the accountability chain if simulation-informed policy causes harm.

**Why it matters for THIS paper:**

- **The paper makes actionable policy claims.** The abstract states that "interventions that shorten waiting time may therefore improve vaccine uptake and may be especially effective when targeted toward populations that are neither strongly trusting nor strongly distrustful." This is a targeting recommendation — it tells policymakers to prioritize neutral-trust populations for wait-time reduction. If this finding does not replicate in other settings, following this recommendation could misallocate resources away from populations that actually need them most.

- **The MWTA metric carries implicit welfare claims.** By translating delay sensitivity into monetary terms (RMB per month of waiting), the paper creates a metric that policymakers could use for cost-benefit analysis. But MWTA is a stated-preference summary, not a welfare measure (the paper acknowledges this in Appendix E4, but the caveat is buried in supplementary material). A policymaker reading only the main text could plausibly use MWTA values as willingness-to-pay estimates in a formal economic evaluation, over-interpreting their policy significance.

- **No stop conditions or minimum quality thresholds.** The paper does not specify conditions under which its findings should not be used to inform policy. For a stated-preference study, relevant thresholds include: minimum response quality (the paper reports 1.8% dominance violations and 0% attribute non-attendance for key attributes — but does not state what level would have been disqualifying), minimum sample size per subgroup (the strongly-distrust group has only n=93), and minimum effect size for policy action.

- **The neutral-trust targeting recommendation has distributional consequences.** If policymakers follow the recommendation to prioritize neutral-trust populations, this means deprioritizing low-trust populations — who are often the most marginalized and vaccine-hesitant. The paper does not discuss this trade-off.

- **No human-in-the-loop requirement.** The paper's findings could be incorporated into automated vaccine scheduling algorithms or resource allocation models without domain-expert review. The paper does not recommend against this.

**Concrete additions (3):**

1. **[§4.3 (Discussion — Implications for Preventive Health Delivery and Equity), Priority: High]** — Add a "Responsible Use" paragraph: "The finding that neutral-trust populations are most delay-sensitive should not be interpreted as a recommendation to deprioritize wait-time reduction for low-trust or high-trust populations. Low-trust populations may face compounded barriers to vaccination — including distrust, access barriers, and informational deficits — that operate independently of waiting time. Targeting wait-time reduction exclusively at neutral-trust populations could exacerbate existing inequities. We recommend that the trust-based heterogeneity finding be used to understand differential responsiveness, not to ration service improvements."

2. **[§4.4 (Discussion — Monetary Interpretation), Priority: Medium]** — Strengthen the MWTA caveat by moving it from the supplementary appendix to the main text: "MWTA values reported in this study are preference-based summary measures derived from stated choices, not welfare estimates or market prices. They should not be used as direct inputs to cost-benefit analysis without acknowledging the assumptions of the random-utility framework, the hypothetical nature of the choice context, and the cultural specificity of the monetary valuations."

3. **[§4.5 (Limitations), Priority: Medium]** — Add a "Replication Requirements Before Policy Application" sentence: "Before the neutral-trust targeting finding is used to inform vaccine delivery policy, replication is recommended in at least one additional setting with different institutional trust dynamics. The small sample size of the strongly-distrust group (n=93) and the cross-sectional nature of the trust measurement limit the reliability of trust-group-specific estimates for policy targeting."

---

## 5. Data Sovereignty & Legal Context

**Gap:** The paper collects data from 1,027 adults in Wuhan, China, through an online survey platform, but does not discuss the data governance framework — including which data protection laws apply, where the data is stored, who has access, and what cross-border data transfer considerations arise if the research is published in an international (potentially US-based) journal.

**Why it matters for THIS paper:**

- **China's Personal Information Protection Law (PIPL, effective November 2021)** imposes specific requirements on personal data collection, including informed consent for the specific purposes of processing, data minimization, and restrictions on cross-border transfer of personal information. The paper's informed consent statement (§Ethics) covers survey participation but does not address data storage, processing, or cross-border transfer.

- **The Data Security Law (DSL, effective September 2021)** classifies certain data relating to public health as "important data" subject to enhanced security requirements. Vaccination preferences from 1,027 residents of Wuhan — a city with particular political-health sensitivity — could arguably fall within this scope, particularly if the data includes geographic identifiers (the paper collects district-level residence information for quota sampling).

- **Cross-border publication context.** If the paper is published in a US-based or European journal, the peer-review process involves transmitting data and analysis materials across borders. The Data Availability Statement says de-identified data "may be made available upon reasonable request" — but PIPL Article 38 requires specific legal mechanisms (standard contracts, security assessments, or certification) for cross-border transfer of personal information, even de-identified data if re-identification is possible.

- **The author is based at UT Dallas (US institution) but collected data in Wuhan.** This creates a US-China data governance interface that the paper does not address. If the survey platform was hosted outside China (e.g., Qualtrics, SurveyMonkey), the data may have been transferred to US servers at the point of collection — a potential PIPL compliance issue.

- **Re-identification risk from preference data.** The paper states data is "de-identified," but DCE data with five attributes per choice task, six tasks per respondent, plus demographic information (age, gender, district, education, smoking, physical activity, medical condition, healthcare access, prior vaccine reaction, institutional trust) creates a high-dimensional profile that could be re-identified, especially for rare combinations in a geographically specific sample (Wuhan districts).

**Concrete additions (3):**

1. **[§Ethics or new §Data Governance, Priority: High]** — Add a "Data Governance" paragraph specifying: (a) which data protection laws apply (PIPL, DSL, and if applicable, the author's US institution's IRB data handling requirements); (b) where the survey data is physically stored (China-based server, US-based cloud, or other); (c) what cross-border data transfer mechanisms, if any, were used; (d) the institutional entity responsible for data stewardship. If the survey was administered through a Chinese platform (e.g., Wenjuanxing, Credamo), state this; if through a US-based platform (e.g., Qualtrics), address the cross-border transfer.

2. **[§Data Availability Statement, Priority: High]** — Revise to address PIPL compliance: clarify what "de-identified" means in practice (which identifiers were removed, whether district-level residence is included in shared data), what re-identification risk assessment was conducted, and what legal mechanism would govern any cross-border data sharing. If data cannot be legally shared cross-border under PIPL, state this honestly rather than offering a conditional availability that may not be executable.

3. **[§2.2 (Participants and Setting), Priority: Medium]** — Add a sentence on the survey platform and data routing: "The survey was administered through [platform name], with data stored on [server location]. [If applicable: Data collection complied with the Personal Information Protection Law of the People's Republic of China (PIPL), including provisions on informed consent for data processing and cross-border data transfer.]"

---

## 6. Missing Voices

**Gap:** The paper's policy recommendations are formulated entirely from the perspective of the researcher-analyst, without engagement with the perspectives of clinicians who administer vaccines, public health administrators who manage delivery systems, community representatives from the populations whose preferences were measured, or ethicists who could assess the societal implications of trust-based targeting.

**Why it matters for THIS paper:**

- **No clinician/practitioner input on DCE attribute design.** The five attributes (waiting time, efficacy, side effects, vaccine origin, cash incentives) were selected based on "prior stated-preference studies" (§2.3) and pilot-tested for comprehension — but there is no indication that vaccination clinicians or public health practitioners reviewed the attribute set for clinical realism. For example: Is a 0–6 month waiting time range clinically realistic? In what vaccination context would a 6-month wait actually occur? Would clinicians consider cash incentives a legitimate policy lever, or would they view this attribute as introducing a confound that doesn't reflect real-world vaccination decisions?

- **No community engagement in instrument development.** The pilot study (n=60, Appendix A.2) tested comprehension and cognitive burden but did not appear to involve community stakeholders in defining which attributes matter to Wuhan residents. The paper does not report whether any community advisory board, local health department representative, or patient advocacy group was consulted in the DCE design. This is particularly important given that the study population has unique pandemic experience — attributes that matter to them (e.g., trust in the specific institutions involved in the 2020 response) may differ from attributes derived from the generic vaccination preference literature.

- **No policymaker perspective on feasibility.** The paper recommends reducing waiting time and targeting neutral-trust populations — but does not consult health administrators about whether wait-time reduction is feasible in Wuhan's vaccination system, what the implementation barriers are, or whether trust-based targeting is operationally possible (how would a clinic identify a patient's trust level?).

- **No ethicist voice on trust-based targeting.** The recommendation to target neutral-trust populations raises an ethical question that the paper does not address: Is it appropriate to use institutional trust as a targeting variable for public health interventions? Trust is correlated with socioeconomic status, education, and political engagement — targeting based on trust could functionally become targeting based on class or political alignment.

- **Missing voice of the data subjects.** The 1,027 respondents consented to a survey about vaccination preferences. The paper does not discuss whether respondents were informed that their data might be used to derive policy recommendations about their own community, or whether they would be comfortable with trust-based targeting as a policy consequence of their participation.

**Concrete additions (3):**

1. **[§4.3 (Discussion — Implications), Priority: High]** — Add a "Stakeholder Engagement" limitation: "The policy implications discussed in this section are derived solely from the analysis of stated preference data. We did not consult with vaccination clinicians, public health administrators, or community representatives in interpreting the findings or assessing the feasibility of the proposed interventions. Future work should engage these stakeholders — particularly Wuhan-area health practitioners and community representatives — to validate whether the trust-based heterogeneity pattern is actionable in practice and whether trust-based targeting is ethically acceptable to the affected communities."

2. **[§2.3 (DCE Attributes and Choice Tasks), Priority: Medium]** — Add a note on attribute selection process: "Attribute selection was informed by prior stated-preference studies and pilot testing for respondent comprehension. The attribute set was not reviewed by vaccination clinicians or public health practitioners for clinical realism, which is a limitation. Future DCE instruments in this domain would benefit from practitioner input on attribute relevance and level plausibility."

3. **[§4.6 (Conclusion) or new §Ethical Implications of Targeting, Priority: Medium]** — Add a sentence on the ethics of trust-based targeting: "Using institutional trust as a targeting variable for vaccination interventions raises ethical questions that warrant community deliberation. Trust is correlated with socioeconomic status, education, and political engagement; targeting interventions based on trust could functionally become targeting based on class or political alignment, potentially exacerbating the inequities that the intervention aims to address."

---

## Summary Table: Proposed Additions Mapped to Paper Sections

| # | Proposed Addition | Section | Priority |
|---|---|---|---|
| 1.1 | Demographic profile table for trust groups + confound check | §3.2 (Results) | High |
| 1.2 | Equity-stratified burden paragraph (urban/rural, education) | §4.3 (Discussion) | High |
| 1.3 | Income benchmarking in sample composition table | Appendix B | Medium |
| 2.1 | Expanded ethics statement (reviewing body, distress protocol, CLD ethics) | §Ethics | High |
| 2.2 | Ethical acknowledgment of CLD framing in Wuhan context | §2.1 (Study Design) | Medium |
| 2.3 | Resolve data availability contradiction (PIPL/governance mechanism) | §Data Availability | Medium |
| 3.1 | Cultural and institutional scope paragraph | §1 (Introduction) | High |
| 3.2 | Strengthened generalizability boundary + replication targets | §4.5 (Limitations) | High |
| 3.3 | Cultural specificity note on institutional trust measure | §2.4 (Measures) | Medium |
| 4.1 | Responsible use paragraph (anti-targeting caveat) | §4.3 (Discussion) | High |
| 4.2 | Strengthen MWTA caveat in main text | §4.4 (Discussion) | Medium |
| 4.3 | Replication requirements before policy application | §4.5 (Limitations) | Medium |
| 5.1 | Data governance paragraph (PIPL, storage, cross-border) | §Ethics or new § | High |
| 5.2 | Revise data availability for PIPL compliance | §Data Availability | High |
| 5.3 | Survey platform and data routing disclosure | §2.2 (Participants) | Medium |
| 6.1 | Stakeholder engagement limitation | §4.3 (Discussion) | High |
| 6.2 | Practitioner input note on attribute selection | §2.3 (DCE Attributes) | Medium |
| 6.3 | Ethics of trust-based targeting | §4.6 (Conclusion) | Medium |

---

## Top-3 Most Important Additions

### 1. Data Governance & Sovereignty Disclosure (Axis 5, Addition 5.1)

**Why most important:** The paper collects health-related preference data from 1,027 Chinese residents through a US-based researcher, with no discussion of PIPL, DSL, data storage location, or cross-border transfer mechanisms. This is not merely a perspective gap — it is a potential legal compliance issue that could affect the paper's publishability and the author's institutional standing. If the data was collected through a US-hosted platform without proper PIPL cross-border transfer mechanisms, the data collection itself may have legal exposure. This must be addressed before publication, not after reviewer comments.

**Specific action:** Add a "Data Governance" paragraph specifying the applicable laws, data storage location, survey platform, and cross-border transfer compliance. Revise the Data Availability Statement to be PIPL-compliant and internally consistent.

### 2. Equity-Stratified Burden Analysis (Axis 1, Addition 1.2)

**Why second most important:** The paper's headline finding is trust-based heterogeneity, but the supplementary data (Appendix D, Table 3) reveals that urban/rural and education-based differences in waiting-time sensitivity are at least as large as the trust-based differences — and these are more directly actionable for equity policy. The paper's current framing directs attention away from these structural inequities and toward a psychological variable (trust) that is harder to intervene on and ethically riskier to target. Surfacing the urban/rural and education gradients in the main text would (a) make the equity claims more empirically grounded, (b) provide more actionable policy targets, and (c) preempt criticism that the paper overlooks structural determinants in favor of psychological ones.

**Specific action:** Add a paragraph in §4.3 reporting the urban/rural (β = −0.130 vs. −0.196) and education (β = −0.201 vs. −0.128) differences in per-month waiting-time sensitivity, and discuss their policy implications alongside the trust heterogeneity.

### 3. Cultural and Institutional Scope Statement (Axis 3, Addition 3.1)

**Why third most important:** The paper's title — "Waiting Time as a Behavioral Barrier to Vaccination Uptake" — implies a general finding about vaccination behavior, but the evidence is from a single city with one of the most distinctive pandemic experiences in human history. A reader, especially a policymaker, could easily over-generalize the findings. The paper's own limitation acknowledgment (§4.5) frames this as a matter of magnitude variation, not qualitative difference — but the nonlinear trust pattern may be a Wuhan-specific artifact. An explicit scoping statement in the Introduction, plus strengthened replication requirements in the Limitations, would honestly bound the claims without diminishing the paper's contribution.

**Specific action:** Add a "Cultural and Institutional Scope" paragraph in §1 after the Wuhan-setting justification, and strengthen §4.5 with a Generalizability Boundary table and minimum replication targets.

---

## Assessment of What the Paper Already Does Well

The paper is not negligent on perspective issues — several are partially addressed:

- **Sample benchmarking (Appendix B):** The paper compares the sample to Wuhan Census on gender, age, residence, and education, with χ² tests — this is above-average rigor for a DCE paper.
- **Post-stratification weighting:** The paper reports that weighted analyses yield substantively similar results, addressing one equity concern.
- **Limitations section (§4.5):** The paper acknowledges stated-preference bias, geographic/temporal specificity, and interpretive nature of the trust mechanism — these are honest acknowledgments.
- **FDR correction (Appendix C3):** Benjamini–Hochberg adjustment for multiple subgroup comparisons is methodologically sound and addresses one form of equity-analysis rigor.
- **Response quality checks (Appendix A):** Dominance tests (1.8%) and attribute non-attendance checks are reported, supporting data quality.
- **AI use declaration:** Appropriately scoped to language editing, with explicit statement that AI was not used for analysis or interpretation.

These existing measures mean the perspective review's role is to **strengthen and make more prominent** what is partially present, rather than to identify wholesale omissions. The most critical additions (data governance, equity-stratified burden, cultural scope) address gaps that are currently absent from the manuscript entirely.

---

## References to Cite

- China PIPL (2021) Personal Information Protection Law of the People's Republic of China — cross-border data transfer requirements (Articles 38–43)
- China Data Security Law (2021) — classification of health-related data
- Gelfand MJ et al. (2011) "Differences between tight and loose cultures." *Science* 332(6033):1100–1104
- Hofstede G (2001) *Culture's Consequences.* 2nd ed. Sage
- Majone G (1989) *Evidence, Argument, and Persuasion in Policy.* Yale UP
- Stone D (2012) *Policy Paradox.* 3rd ed. Norton
- Stanford HAI (2025) "Simulating Human Behavior with AI Agents"
- Gichoya JW et al. (2022) "AI pitfalls and what not to do." *Radiology*
- Herd P, Moynihan DP (2018) *Administrative Burden.* Russell Sage
- Buolamwini J, Gebru T (2018) "Gender Shades." *FAT*⁠*Conference*
