"""
Phase 02: Python for ML
Topic: 02 - Pandas Basics to Advanced
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. BEGINNER: Creating DataFrames & Inspecting
# ==============================================================================
print("--- BEGINNER: DataFrame Creation ---")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, np.nan, 35, 45, 22],
    "Department": ["Engineering", "HR", "Engineering", "Sales", "HR"],
    "Salary": [85000, 60000, 120000, 95000, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nDataFrame Info (Checking for Nulls):")
print(df.info())


# ==============================================================================
# 2. INTERMEDIATE: Cleaning & Filtering Data
# ==============================================================================
print("\n--- INTERMEDIATE: Data Cleaning ---")

# 1. Handling Missing Data (Imputation)
# Fill missing age with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing salary with the mean salary of their department
df['Salary'] = df.groupby('Department')['Salary'].transform(lambda x: x.fillna(x.mean()))

print("Cleaned DataFrame:")
print(df)

# 2. Filtering
# Find all Engineers making over 80k
high_earning_engineers = df[(df['Department'] == 'Engineering') & (df['Salary'] > 80000)]
print("\nHigh Earning Engineers:")
print(high_earning_engineers)


# ==============================================================================
# 3. ADVANCED: GroupBy, Aggregation & Feature Engineering
# ==============================================================================
print("\n--- ADVANCED: Aggregation ---")

# Aggregating multiple metrics per department
dept_stats = df.groupby('Department').agg(
    Employee_Count=('Name', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Max_Age=('Age', 'max')
)
print("Department Statistics:")
print(dept_stats)

print("\n--- ADVANCED: Feature Engineering ---")
# Creating a new categorical feature based on Age
df['Experience_Level'] = pd.cut(df['Age'], bins=[0, 30, 40, 100], labels=['Junior', 'Mid', 'Senior'])
print(df[['Name', 'Age', 'Experience_Level']])
