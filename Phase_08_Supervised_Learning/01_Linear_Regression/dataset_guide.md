# Dataset Guide: Linear Regression Target Datasets

When studying Linear Regression, you must work with tabular, continuous target datasets. 

### Recommended Standard Datasets
1. **California Housing Dataset** (Built into Scikit-learn)
   - **Target**: House Prices.
   - **Characteristics**: Large number of rows, distinct geographical clusters.
   - **Preprocessing Challenge**: Requires heavy scaling due to different units (Income in 10k, Population in thousands, Rooms in singles).

2. **Ames Housing Dataset** (Kaggle)
   - **Target**: SalePrice.
   - **Characteristics**: Contains 79 explanatory variables describing every aspect of residential homes in Ames, Iowa.
   - **Preprocessing Challenge**: Perfect for practicing **One-Hot Encoding** (converting categorical variables like 'Neighborhood' into binary vectors) and **Lasso Regression** (L1 Regularization) to drop useless features.

### Preprocessing Strategy for Linear Regression
1. **Missing Values**:
   - Linear algorithms cannot handle `NaN` mathematically. 
   - Strategy: Impute missing continuous variables with the `median`. Impute categorical variables with the `mode`.
2. **Encoding Strategy**:
   - Must use One-Hot Encoding (`pd.get_dummies` or `OneHotEncoder`). 
   - **CRITICAL**: Use `drop_first=True` to avoid the "Dummy Variable Trap" (perfect multicollinearity).
3. **Normalization/Scaling**:
   - If using Gradient Descent or Regularization (Ridge/Lasso), **StandardScaler** (Z-score normalization) is mandatory. Without it, features with larger ranges will dominate the cost function.
4. **Leakage Risks**:
   - Ensure you perform `.fit_transform()` on the **Train set**, but ONLY `.transform()` on the **Test set**. Fitting the scaler on the entire dataset leaks statistical information (mean, variance) from the future (test data) into the model.
