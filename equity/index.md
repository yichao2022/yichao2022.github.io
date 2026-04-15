---
layout: default
title: "Equity & Policy Impact | Yichao Jin, PhD"
---

<!-- MathJax Engine (For LaTeX) -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- Mermaid Engine (For Diagrams) -->
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ 
    startOnLoad: true, 
    theme: 'neutral',
    securityLevel: 'loose',
    fontFamily: 'Inter, sans-serif'
  });
</script>

# Administrative Burden & Equity Diagnostics

My research identifies the Hidden Majority (45%) who are paralyzed by administrative friction ($\kappa$) rather than policy opposition. By quantifying this Equity Tax, I help labs design more inclusive interventions.

In alignment with community-centered, data-driven public policy, my research examines how seemingly minor logistical hurdles create outsized barriers for marginalized groups. Public policy too often focuses on macro-level goals, but true equity is determined in the micro-frictions of implementation.

**"Administrative Sludge"** refers to the bureaucratic hurdles and paperwork in policy design that, cumulatively, lead to massive disparities in take-up among vulnerable populations.

<div class="mermaid">
graph TD
  A[100% Target Population] --> B{Administrative Sludge}
  B -- low friction --> C[55% Successful Adopters]
  B -- high kappa/friction --> D[45% Neutral Swing Group - LOST]
  style D fill:#f96,stroke:#333,stroke-width:4px
</div>

## The Anatomy of Inaction: How $\kappa$ Drives Inequality

At the core of the equity gap lies **$\kappa$ (Administrative Friction)**. 

To quantify this, we look at the **Friction-Adjusted Utility**:

$$Utility = V(Benefit) - \kappa_{Friction}$$

Where $U(a)$ represents the baseline utility of taking a policy action, and $\kappa_{sludge}$ represents the immediate cognitive and temporal drain of navigating administrative hurdles.

By applying **$\beta-\delta$ modeling**, my structural framework reveals that $\kappa$ does not affect all groups equally. Instead, it acts as a regressive "tax on the poor and the time-constrained." For populations with high present-bias ($\beta$) and low baseline institutional trust ($\delta$), the immediate costs of $\kappa$ heavily outweigh delayed benefits. The result is the **Anatomy of Inaction**—not active resistance to policy, but a systemic paralysis induced by friction.

## The "Hidden Majority": Where We Lose 45%

In my research examining intertemporal choices, a critical data point emerged: roughly **45% of the target population** are not actively opposed to public goals (e.g., vaccination). Instead, they belong to a **"Neutral Swing Group"**. 

Because they lack strong proactive motivation, even minor barriers can indefinitely delay their compliance, causing them to fall through the cracks of public initiatives. The Sankey diagram below illustrates exactly where these populations are lost to friction.

```mermaid
sankey-beta
    %% Source, Target, Value
    Target Population, Adopters (Low Friction), 55
    Target Population, Admin Friction, 45
    Admin Friction, Complexity, 15
    Admin Friction, Time Scarcity, 20
    Admin Friction, Mistrust, 10
    
    Complexity, Neutral Swing Group, 15
    Time Scarcity, Neutral Swing Group, 20
    Mistrust, Neutral Swing Group, 10
```

## Mapping the Equity Gap

When we compare populations burdened by $\kappa$ versus those unburdened, the disparities in policy engagement become stark. The following heatmap table illustrates how different behavioral constraints interact with administrative sludge to widen the equity gap.

| Behavioral Persona | Institutional Trust ($\delta$) | Present Bias ($\beta$) | Friction Sensitivity ($\kappa$) | Policy Take-up Rate | Risk of Exclusion |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **High-Resource Advocates** | High | Low | Low | 🟩 **85%** | ⬜ Minimal |
| **Constrained Compliers** | Medium | Medium | Medium | 🟨 **55%** | 🟨 Moderate |
| **The Neutral Swing Group** | Low | High | High | 🟧 **15%** | 🟧 High |
| **Marginalized/Unreached** | Very Low | Very High | Extreme | 🟥 **<5%** | 🟥 Severe |

*Note: The structural burden is disproportionately carried by those with the least cognitive bandwidth to spare. Interventions must target the $\kappa$ parameter to convert the orange/red zones into green.*

## Redesigning for Possibility

The evidence is clear: when we design policies without accounting for the true cost of administrative burdens, we fail our most vulnerable constituents. Redesigning policy for equity means aggressively auditing and eliminating sludge. By centering community realities and deploying data-driven friction-reduction, we can build public programs that truly serve everyone.

👉 **[Download the JMP (Policy & Equity Focus)](/jmp.pdf)**

---
### Open Source & Reproducibility
Explore the interactive code, models, and simulation sandbox in the [Digital-Choice-Manifesto](https://github.com/yichao2022/Digital-Choice-Manifesto) repository.
