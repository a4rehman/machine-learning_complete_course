# Cheatsheet: Linear Regression

### The Math
- **Hypothesis**: $h_\theta(x) = \theta_0 + \theta_1x_1 + \dots + \theta_nx_n$
- **MSE Cost Function**: $J(\theta) = \frac{1}{2m}\sum (\hat{y} - y)^2$
- **Gradient Update**: $\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)$
- **Normal Equation (OLS)**: $\theta = (X^T X)^{-1} X^T y$

### Assumptions of Linear Regression (L.I.N.E.)
1. **Linearity**: The relationship between X and Y is linear.
2. **Independence**: Observations are independent of each other (no autocorrelation).
3. **Normality**: The residuals (errors) are normally distributed.
4. **Equal Variance (Homoscedasticity)**: The variance of residuals is constant across all X.

### Evaluation Metrics
- **MAE (Mean Absolute Error)**: Average of absolute errors. Highly interpretable. Robust to outliers.
- **MSE (Mean Squared Error)**: Punishes large errors aggressively.
- **RMSE (Root MSE)**: Brings MSE back to the original unit scale.
- **R-Squared ($R^2$)**: 0 to 1 scale. Represents the percentage of variance in Y explained by X.

### Regularization Methods
When you have high variance (overfitting):
- **Ridge (L2)**: Adds squared magnitude of weights to cost. Shrinks weights close to zero but rarely exactly zero.
- **Lasso (L1)**: Adds absolute magnitude of weights to cost. Can shrink weights exactly to ZERO (acts as feature selection).
- **ElasticNet**: Combines both L1 and L2 penalties.
