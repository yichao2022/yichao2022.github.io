---
title: "Clinical Simulation | Yichao Jin, PhD"
layout: page
---

# Precision Behavioral Interventions in Clinical Settings

# The Clinical Bottleneck: Decoding "Intervention Fatigue"

Medical systems possess the world's richest EHR and patient follow-up data. Yet, traditional "nudges"—like SMS reminders or static financial incentives—often fail in real-world clinical settings due to patient non-adherence and trial attrition.

The missing link is the structural quantification of **Cognitive Friction ($\kappa$)** and **Trust Depreciation ($\delta$)**. A nudge that works on Day 1 often triggers avoidance by Day 14. 

## The Core Mechanism: Present Bias & Patient Heterogeneity

To understand why a patient postpones scheduling a critical screening or delays vaccination despite optimal incentives, we must look at the structural mechanics of their decision-making. 

Our engine models this through an augmented Bellman Equation that embeds specific behavioral biases directly into the patient's value function:

$$V(s_t) = \max_{a_t} \{ U(a_t, \kappa) + \beta \delta E [V(s_{t+1})] \}$$

*   **$\kappa$ (Administrative/Cognitive Friction)**: The mental bandwidth required to navigate the clinical system. 
*   **$\beta$ (Present Bias)**: The psychological tendency to heavily discount future health benefits in favor of immediate comfort.
*   **$\delta$ (Trust Capital)**: The evolving trust in the medical provider, which depreciates if interventions are poorly timed or overly aggressive.

### Technical Implementation: Patient-Level Value Iteration

Below is a structural cut of the `02_bellman_engine.R` solver, illustrating how individual patient parameters are evaluated dynamically to predict dropout risks:

```R
# ---------------------------------------------------------
# TRIBE-v2: Patient-Level Heterogeneous Bellman Solver
# ---------------------------------------------------------

solve_patient_value <- function(state, beta, delta, kappa, incentive) {
  # 1. U(a_t, kappa): Utility adjusted for cognitive/administrative friction
  utility_adhere <- incentive - kappa
  utility_delay  <- 0  # The baseline comfort of inaction
  
  # 2. Expected Future Value
  # Incorporating Present Bias (beta) and Trust Capital (delta)
  expected_future_value <- compute_ev(state + 1)
  discounted_future <- beta * delta * expected_future_value
  
  # 3. Dynamic Bellman Operator
  # V(s_t) = max { U(a_t, \kappa) + \beta \delta E[V(s_{t+1})] }
  v_adhere <- utility_adhere + discounted_future
  v_delay  <- utility_delay + discounted_future
  
  # If v_delay > v_adhere, the patient exhibits 'Present Bias' 
  # and structurally drifts from the clinical path.
  return(max(v_adhere, v_delay))
}
```

This structural approach explains why even perfectly rational economic incentives fail when $\kappa$ (friction) overwhelms the discounted future benefit.

## Visualizing the Clinical Reality

<div align="center">
  <div class="mermaid">
stateDiagram-v2
    direction LR
    %% Agent progressing towards a health goal
    [*] --> Scheduled_for_Screening : Optimal Pathway Begins
    Scheduled_for_Screening --> Compliant : High Trust (δ) / Low Friction (κ)
    
    %% Getting trapped
    Scheduled_for_Screening --> Delayed : Present Bias (β) triggers Delay
    Delayed --> Delayed : High Friction (κ) creates "Delay Trap"
    
    %% Phase transitions based on structural parameters
    Delayed --> Compliant : Nudge + Low Friction override
    Delayed --> System_Dropout : Trust (δ) decays below threshold
    
    Compliant --> [*] : Health Goal Achieved
    System_Dropout --> [*] : Lost to Follow-up
  </div>
  <p><em><strong>Figure 1. Decision Drift:</strong> This visualization maps the empirical divergence between the optimal clinical pathway and actual patient adherence. It highlights how the accumulation of $\kappa$ (cognitive friction) and the decay of $\delta$ (trust capital) structurally push patients into "delay" loops, ultimately leading to clinical trial dropout or non-compliance.</em></p>
</div>

---
*Powered by TRIBE-v2 (Trust-Reinforced Intertemporal Behavioral Engine) - Tailored for Precision Health Interventions.*
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

