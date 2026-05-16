# Exercises: Linear Regression

### Beginner Tasks
**Task 1: The Scikit-Learn Loop**
- **Objective**: Import `LinearRegression` from `sklearn`. Create synthetic data using `np.random`. Train the model and extract `model.coef_` and `model.intercept_`.
- **Expected Output**: Printed weight and bias matching your synthetic generation formula.
- **Difficulty**: ⭐

**Task 2: Plot the Fit**
- **Objective**: Use Matplotlib to scatter plot your synthetic data. Then plot the learned regression line (prediction) on top of the scatter plot in red.
- **Difficulty**: ⭐

### Intermediate Problems
**Task 3: Cost Function Implementation**
- **Objective**: Write a pure Python/NumPy function `compute_mse(y_true, y_pred)` that mathematically calculates the Mean Squared Error without using sklearn.
- **Expected Output**: A float representing the cost.
- **Difficulty**: ⭐⭐

**Task 4: Feature Scaling Impact**
- **Objective**: Create a dataset with two features: one ranging from 0-1, and one from 0-1,000,000. Try training a Gradient Descent model *without* scaling. Observe the `NaN` errors. Then, apply `StandardScaler` and retrain.
- **Difficulty**: ⭐⭐

### Advanced ML Challenges
**Task 5: Ridge Regression Implementation**
- **Objective**: Modify the Gradient Descent class in `practice.py` to include L2 Regularization (Ridge). Update the cost function and gradient math.
- **Hints**: The cost function adds `+ lambda * sum(weights^2)`. The gradient update adds `+ lambda * weights`.
- **Difficulty**: ⭐⭐⭐

### Debugging Tasks
**Task 6: The Learning Rate Bug**
- **Objective**: Set the learning rate in your scratch Gradient Descent model to `10.0`. Print the loss history. Explain in writing why the loss explodes to infinity.
