# Mini Project: Real Estate Valuation Model

### Objectives
Build a production-ready Linear Regression pipeline that predicts house prices based on historical real estate data. You will handle missing values, scale features, train the model, and interpret the feature weights.

### Dataset Structure (California Housing)
Use `sklearn.datasets.fetch_california_housing`.
- **Features**: `MedInc` (Income), `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`.
- **Target**: `MedHouseVal` (Median House Value in $100k).

### Preprocessing & Pipeline
1. **Load Data**: Convert the sklearn bunch object into a Pandas DataFrame.
2. **Exploratory Data Analysis (EDA)**: Plot a correlation heatmap using Seaborn. Identify which feature has the highest correlation with the target.
3. **Feature Engineering**: Create a new feature: `Rooms_per_Household = AveRooms / AveOccup`.
4. **Scaling**: Apply `StandardScaler` to all features. (CRITICAL: fit only on training data, transform on test).

### Model Selection & Training
1. Train a standard `LinearRegression` model.
2. Extract and print the coefficients (weights) alongside their feature names. 
3. **Business Insight**: Write a 2-sentence conclusion on which feature adds the most value to a house.

### Evaluation Metrics
- Calculate **RMSE** (Root Mean Squared Error) to get the error in real dollars.
- Calculate **R-Squared ($R^2$)** to understand how much variance your model explains.

### Deployment Ideas (MLOps Extension)
- Export the `scaler` and `model` using the `joblib` library.
- Write a 10-line FastAPI `app.py` that takes a JSON payload of house features, scales them, and returns the predicted price.
