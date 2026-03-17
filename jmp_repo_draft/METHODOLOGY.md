# Empirical Methodology & Parameter Recovery

This document outlines the statistical models used to derive the behavioral findings in the JMP.

## 1. Structural Discounting Parameters
We fit two competing models to the observed decay in vaccination utility over time:

### Hyperbolic Discounting
$$D(t) = \frac{1}{1 + Kt}$$
- **Result**: $K = 0.225$
- **Interpretation**: This non-linear decay indicates "Present Bias," where immediate costs (wait time) are disproportionately weighted against future health benefits.

### Exponential Discounting
$$D(t) = e^{-rt}$$
- **Result**: $r = 0.160$
- **Comparison**: The Hyperbolic model consistently yields a lower RMSE, confirming that respondents follow time-inconsistent behavior patterns.

## 2. Marginal Willingness to Accept (MWTA)
The shadow price of waiting time is calculated as the ratio of the time coefficient to the price (incentive) coefficient:
$$MWTA_{WaitTime} = - \frac{\beta_{WaitTime}}{\beta_{Incentive}}$$

Based on our Mixed Logit estimation:
- **Baseline MWTA**: ~47 RMB/hour.
- **Urban Premium**: Urban residents exhibit a higher MWTA, reflecting higher opportunity costs of time.

## 3. Interaction Models
We use interaction terms to test the "Trust as a Buffer" hypothesis:
$$U_{ij} = \beta_1 WaitTime_j + \beta_2 (WaitTime_j \times Trust_i) + \dots$$
A significant positive $\beta_2$ indicates that higher trust levels mitigate the disutility of waiting.
