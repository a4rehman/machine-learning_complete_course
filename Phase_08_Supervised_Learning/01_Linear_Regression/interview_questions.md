# Interview Questions: Linear Regression

### Beginner Questions

**1. What is the difference between classification and regression?**
**Answer:** Regression predicts a continuous numerical output (e.g., house price, temperature), whereas classification predicts a discrete categorical label (e.g., Spam vs Not Spam, Cat vs Dog).

**2. Explain what R-squared means to a non-technical stakeholder.**
**Answer:** "R-squared tells us how much of the guesswork our model removes. If R-squared is 0.80, it means our model accounts for 80% of the reasons why house prices change. The remaining 20% is due to factors we don't have data on."

### Intermediate Questions

**3. What is multicollinearity and why is it a problem?**
**Answer:** Multicollinearity occurs when independent variables are highly correlated with each other (e.g., BMI and Weight). It makes it mathematically difficult for the model to isolate the individual effect of each feature. While it doesn't always hurt predictive accuracy, it destroys interpretability because the weights become wildly unstable. It is fixed by dropping correlated features or using PCA.

**4. When would you use Mean Absolute Error (MAE) instead of Mean Squared Error (MSE)?**
**Answer:** You use MAE when your dataset has heavy outliers and you don't want your model to overreact to them. Because MSE squares the error, a single massive outlier will drastically skew the cost function.

### Advanced Engineering / Math Questions

**5. Why do we not use the Normal Equation (OLS) for all linear regression problems instead of Gradient Descent?**
**Answer:** The Normal Equation is $w = (X^T X)^{-1} X^T y$. Inverting the matrix $X^T X$ has a time complexity of roughly $O(n^3)$ where $n$ is the number of features. If we have 100,000 features, matrix inversion becomes computationally impossible or extremely slow. Gradient Descent scales much better to high-dimensional datasets.

**6. Explain heteroscedasticity.**
**Answer:** It is a violation of the equal variance assumption. It means the spread of the residuals (errors) changes as the predicted value changes. For example, predicting income based on age: the error variance for 20-year-olds is small (everyone makes entry-level salary), but for 50-year-olds it's huge (some are CEOs, some are unemployed). It indicates your model is missing a key interaction term or feature.

### System Design / Production

**7. How do you deploy a massive ensemble of Linear Regression models (e.g., one for each zip code) in production with ultra-low latency?**
**Answer:** Because Linear Regression is purely a dot product $\hat{y} = w^T X + b$, I wouldn't use heavy Python containers. I would extract the learned weights for all zip codes and store them in an in-memory key-value database like Redis. The inference service (written in Go or Rust for speed) would fetch the weights by zip code and compute the dot product in microseconds, avoiding standard ML serving frameworks entirely.
