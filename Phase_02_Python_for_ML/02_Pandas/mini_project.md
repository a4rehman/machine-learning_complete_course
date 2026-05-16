# Mini Project: Exploratory Data Analysis (EDA) on Titanic

## Problem Statement
The Titanic dataset is the most famous beginner dataset in Machine Learning. Before building a model to predict who survived, you must understand the data. 
**Your Task**: Perform an EDA pipeline using Pandas.

## Dataset
You can load the dataset directly from seaborn (which returns a Pandas DataFrame):
```python
import seaborn as sns
df = sns.load_dataset('titanic')
```

## Step-by-Step Implementation

1. **Initial Inspection**:
   - Print the `.info()` and `.describe()`.
   - Identify which columns have missing values.
2. **Data Cleaning**:
   - The `age` column has missing values. Fill them with the median age of the passengers.
   - The `deck` column has too many missing values. Drop the entire column using `.drop()`.
3. **Feature Engineering**:
   - Create a new column called `family_size` which is the sum of `sibsp` (siblings/spouses) and `parch` (parents/children) + 1 (themselves).
4. **Analytics (The Business Logic)**:
   - Use `.groupby()` to calculate the survival rate (`survived.mean()`) grouped by `class` (First, Second, Third class).
   - Use `.groupby()` to calculate the survival rate grouped by `sex`.

## Expected Output
A clean Python script/notebook that prints out the survival probabilities. You should mathematically prove the famous historical rule: "Women and children first, and First-Class passengers had a massive advantage."
