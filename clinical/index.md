---
title: "Clinical Simulation | Yichao Jin, PhD"
layout: page
---

# Clinical Decision Diagnostics & Patient Adherence

In modern medical systems, the most robust predictive models often fail at the last mile: human behavior. Despite optimal clinical pathways, SMS reminders, and well-designed incentives, patients frequently exhibit non-adherence, delayed screenings, or drop out of clinical trials. 

By applying structural behavioral economics and neuro-computational models, we can decode and predict these adherence failures. The missing link is the structural quantification of **Cognitive Friction ($\kappa$)**, **Present Bias ($\beta$)**, and **Trust Depreciation ($\delta$)**.

## Visualizing Patient Decision Drift

Why does a patient postpone scheduling a critical screening or delay preventive care despite knowing the benefits? We model this structurally as **Patient Decision Drift**—the transition from optimal medical intent into a state of indefinite delay, governed by specific behavioral parameters.

<div align="center">
  <div class="mermaid">
stateDiagram-v2
    direction LR
    
    [*] --> Intent : Medical Recommendation
    
    Intent --> Adherence : Proactive Action (Low β, Low κ)
    Intent --> Delay : Friction (κ) > Utility
    Intent --> Delay : Present Bias (β) Dominates
    
    state Delay {
        direction TB
        Procrastination --> CognitiveFatigue : Repeated Hurdles
        CognitiveFatigue --> ChronicNonAdherence : Trust (δ) Decays
    }
    
    Delay --> Adherence : Intervention / Friction Reduction
    Delay --> [*] : Loss to Follow-up
    Adherence --> [*] : Health Outcome Realized
  </div>
  <p><em><strong>Figure 1. Patient Decision Drift:</strong> This state diagram maps how individuals transition from clinical "Intent" to "Delay" when administrative friction ($\kappa$) outweighs utility, or when present bias ($\beta$) heavily discounts future health outcomes.</em></p>
</div>

## Tech Spotlight: Local Privacy-Preserving AI

A critical challenge in applying advanced AI to clinical settings—especially in neuro-ethics, behavioral mapping, and decision science—is the privacy of Electronic Health Records (EHR). Relying on cloud-based LLM APIs introduces significant friction regarding HIPAA compliance, data sovereignty, and ethical boundaries.

To solve this, **TRIBE v2 (Trust-Reinforced Intertemporal Behavioral Engine)** is structurally optimized for **Apple Silicon and Metal Performance Shaders (MPS)** via the MLX framework. 

This architectural choice allows us to deploy "Local System 2" reasoning models directly on internal medical workstations. By running deep behavioral digital twin simulations **100% locally and offline**, we achieve high-fidelity predictions of patient adherence while ensuring sensitive patient data never leaves the hospital's secure environment.

## Case Study: Quantifying the Friction of Preventive Healthcare

My Job Market Paper serves as a foundational case study in applying this methodology to real-world clinical behavior.

To understand why individuals delayed preventive healthcare (vaccination timing) despite overwhelming public health urgency, I designed a discrete choice experiment to map the intertemporal decisions of populations facing varying levels of administrative and cognitive friction. 

By integrating these choices into a structural econometric framework, the research successfully **recovered core behavioral parameters** directly from empirical decision data:
- **Quantifying $\kappa$**: Measuring exactly how much "sludge" (e.g., confusing scheduling platforms, logistical delays, wait times) it takes to deter an otherwise willing patient.
- **Isolating $\beta$ and $\delta$**: Disentangling procrastination driven by present bias from non-adherence driven by systemic mistrust.

This approach transitions patient adherence from an unpredictable, qualitative frustration into a calculable, actionable metric for clinical trial designers, public health policymakers, and neuro-ethics researchers.

---
*Powered by TRIBE-v2 (Trust-Reinforced Intertemporal Behavioral Engine) - Tailored for Precision Health Interventions and Local Clinical AI.*

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>