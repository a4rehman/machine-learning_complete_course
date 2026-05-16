# Quiz: Linear Regression Fundamentals

**1. What is the primary objective of Linear Regression?**
A) To separate data into distinct classes.
B) To find the line that maximizes the margin between points.
C) To minimize the Mean Squared Error between predicted and actual continuous values.
D) To reduce the dimensionality of the dataset.

**2. In Gradient Descent, what happens if the learning rate ($\alpha$) is set too high?**
A) The model converges instantly.
B) The algorithm oversteps the global minimum, causing the cost to diverge (explode to infinity).
C) The model severely overfits the training data.
D) The algorithm stops updating weights.

**3. Which matrix operation is required for Ordinary Least Squares (OLS) Normal Equation?**
A) Matrix Multiplication only
B) Matrix Addition
C) Matrix Inversion
D) Eigenvalue Decomposition

**4. Linear regression is considered a:**
A) High Bias, Low Variance model
B) Low Bias, High Variance model
C) High Bias, High Variance model
D) Low Bias, Low Variance model

**5. True or False: Feature scaling (Standardization/Normalization) is strictly required for the OLS Normal Equation.**
A) True
B) False

---
### Answers
1. **C** (Linear regression targets continuous variables by minimizing MSE).
2. **B** (A learning rate that is too large causes divergence).
3. **C** (The formula $(X^TX)^{-1}X^Ty$ requires inverting $X^TX$. This makes it slow for huge datasets).
4. **A** (It makes a strong assumption about a linear relationship, resulting in high bias, but is stable, resulting in low variance).
5. **False** (OLS is analytically solved and scale-invariant. Scaling is required for *Gradient Descent*, not OLS).
