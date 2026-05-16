# Topic Name: Linear Regression

# Introduction
Linear regression is the foundational stepping stone of machine learning. Before neural networks and complex ensembles, there is the simple, powerful idea of drawing a line of best fit through data points. It attempts to model the relationship between two variables by fitting a linear equation to observed data. 

# Why This Matters
In the industry, simple models scale best. Linear regression provides incredible interpretability—you can explain exactly *why* a model made a prediction to business stakeholders. It's heavily used in economics, finance, capacity planning, and baseline modeling for complex ML pipelines.

# Core Concepts
- **Dependent Variable (Y)**: The target we want to predict (e.g., House Price).
- **Independent Variable (X)**: The feature(s) we use to predict Y (e.g., Square Footage).
- **Weights/Coefficients (w)**: The learned importance of each feature.
- **Bias/Intercept (b)**: The baseline prediction when all X are zero.

# Mathematical Intuition
Imagine plotting a scatter plot of house sizes vs. prices. The goal of linear regression is to draw a straight line that minimizes the total distance between the line and every single data point. We measure this distance as the "error."

# Mathematical Formulas
1. **Hypothesis (Prediction Equation)**:
   $$ \hat{y} = w^T X + b $$
2. **Cost Function (Mean Squared Error - MSE)**:
   $$ J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2 $$
3. **Gradient Descent Updates**:
   $$ w = w - \alpha \frac{\partial J}{\partial w} $$
   $$ b = b - \alpha \frac{\partial J}{\partial b} $$

# Internal Working
Linear Regression typically solves for weights using one of two methods:
1. **Ordinary Least Squares (OLS)**: A closed-form mathematical solution (Normal Equation). Solves for weights instantly but requires matrix inversion.
2. **Gradient Descent**: An iterative optimization algorithm. It starts with random weights and takes small steps (learning rate $\alpha$) downhill along the gradient of the cost function until it reaches the minimum error.

# Algorithm Mechanics
- **Training**: Computing the gradient of the MSE with respect to weights, updating weights iteratively.
- **Prediction**: A simple dot product of weights and input features. Very fast $O(k)$ where $k$ is the number of features.
- **Hyperparameters**: Learning Rate ($\alpha$), Number of Epochs.

# Performance Analysis
- **Time Complexity (Training OLS)**: $O(n^2 \cdot m)$ or $O(n^3)$ due to matrix inversion.
- **Time Complexity (Gradient Descent)**: $O(k \cdot m)$ per iteration.
- **Inference/Prediction**: $O(k)$. Extremely fast, easily deployed on low-power edge devices.

# Bias-Variance Discussion
Linear regression is a **high-bias, low-variance** model. It assumes the data has a strict linear relationship. If the data is highly non-linear (like a sine wave), it will **underfit** (high bias). However, because it is simple, it is highly resilient to overfitting (low variance) compared to deep decision trees.

# Overfitting vs Underfitting
- **Underfitting**: Model is too simple (just a flat line). Fix by adding polynomial features (Polynomial Regression).
- **Overfitting**: Rare in basic linear regression, but can happen if you have more features than rows ($k > m$). Fix using Regularization (Ridge/Lasso).

# Debugging ML Models
- If Cost ($J$) goes up instead of down: Your learning rate $\alpha$ is too high.
- If Cost ($J$) drops too slowly: Your learning rate $\alpha$ is too low.
- If weights become `NaN`: Exploding gradients. Scale your features using Standard Scaler.

# Best Practices
1. **Always scale your data** before using Gradient Descent.
2. **Check Assumptions**: Linear regression assumes Linearity, Independence, Homoscedasticity, and Normality of errors (LIHN).
3. **Use as a Baseline**: Always build a Linear/Logistic regression before training a Neural Network.

# Common Mistakes
- **Forgetting to scale features**: Causes gradient descent to zig-zag inefficiently.
- **Ignoring Multicollinearity**: Having features that are highly correlated with each other (e.g., 'Yearly Salary' and 'Monthly Salary') destroys the interpretability of weights.

# Real-World Applications
- **Finance**: CAPM (Capital Asset Pricing Model).
- **Sales**: Forecasting quarterly revenue based on marketing spend.
- **Analytics**: Estimating the impact of a UI change on page load times.

# Production Engineering
- **Deployment**: Linear regression weights can simply be extracted as a JSON array `[w1, w2, b]` and evaluated in pure JavaScript on the frontend. No massive ML server required.

# Summary
Linear Regression is the "Hello World" of Machine Learning. It teaches you the core ML loop: Define a Hypothesis, measure Error with a Cost Function, and Optimize with Gradient Descent.
