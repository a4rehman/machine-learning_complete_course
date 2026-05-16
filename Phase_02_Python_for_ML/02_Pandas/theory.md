# Pandas for Machine Learning

## Introduction
While NumPy provides the raw computational horsepower for arrays and matrices, **Pandas** provides the high-level data structures (DataFrames) to work with tabular data. If you have ever used Microsoft Excel or SQL, Pandas is essentially Excel/SQL on steroids, driven by Python.

## Why This Topic Matters
In real-world Machine Learning, data is never a perfect, clean mathematical matrix. It comes as messy CSV files, SQL tables, or JSONs with missing values, string columns, and weird date formats. Pandas is the industry standard tool for **Data Wrangling and Exploratory Data Analysis (EDA)**. You will spend 80% of your time as an ML Engineer using Pandas to clean data before ever touching an ML model.

## Core Concepts
1. **Series**: A 1-dimensional labeled array (basically a single column).
2. **DataFrame**: A 2-dimensional labeled data structure with columns of potentially different types (like a spreadsheet or SQL table).
3. **Index**: The "row labels" of your DataFrame. Very powerful for fast lookups.

## Mathematical Intuition & Internal Working
Pandas is built *directly on top of NumPy*. 
Under the hood, a Pandas DataFrame is actually a collection of NumPy arrays (one array per column data type) managed by a "Block Manager". 
Because it relies on NumPy, operations on Pandas columns are vectorized and extremely fast, provided you avoid using `.apply()` or writing Python `for` loops.

## Python Examples

*Loading and Viewing Data:*
```python
import pandas as pd

# Load data
df = pd.read_csv("dataset.csv")

# View the first 5 rows
print(df.head())

# Get summary statistics (mean, min, max for numerical columns)
print(df.describe())
```

*Data Manipulation:*
```python
# Filtering: Get all rows where Age is greater than 30
adults = df[df['Age'] > 30]

# Grouping: Get the average salary per department
avg_salary = df.groupby('Department')['Salary'].mean()
```

## Advantages
- **Flexibility**: Handles missing data (`NaN`) gracefully.
- **Heterogeneous Data**: Can store integers, floats, strings, and dates in the same DataFrame (in separate columns).
- **Integration**: Has built-in methods to connect to SQL databases, read JSON, Parquet, and Excel files.

## Disadvantages
- **Memory Heavy**: Pandas typically requires RAM equal to 5x to 10x the size of the dataset on disk. Loading a 2GB CSV might consume 15GB of RAM.
- **Single-Threaded**: By default, Pandas only uses one CPU core.

## Best Practices
- **Avoid Loops**: Never use `.iterrows()` unless absolutely necessary. It is painfully slow.
- **Vectorize**: Use built-in Pandas methods (`df['A'] + df['B']`) instead of `.apply()` where possible.
- **Use Parquet**: For large datasets, stop using `.csv`. Save files as `.parquet` to preserve data types and drastically speed up load times.

## FAANG Interview Notes
- **Question**: "What is the difference between `loc` and `iloc`?"
- **Answer**: "`loc` is label-based indexing (e.g., finding a row by its index name 'Row_A'), while `iloc` is integer-position based indexing (e.g., finding the 0th row in memory, regardless of its label)."

## Summary
Pandas is the Swiss Army knife for Data Engineering. Before you feed data into Scikit-Learn or TensorFlow, you will use Pandas to fill missing values, drop bad columns, and encode text into numbers.
