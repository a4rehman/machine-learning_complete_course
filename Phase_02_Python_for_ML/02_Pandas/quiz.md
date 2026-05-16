# Quiz: Pandas for ML

**1. What is the fundamental difference between a Pandas Series and a DataFrame?**
A) A Series holds strings, a DataFrame holds numbers.
B) A Series is 1-dimensional, a DataFrame is 2-dimensional.
C) A Series is immutable, a DataFrame is mutable.
D) There is no difference.

**2. Which method gives you a statistical summary (count, mean, std, min, max) of all numerical columns in a DataFrame?**
A) `df.summary()`
B) `df.info()`
C) `df.describe()`
D) `df.stats()`

**3. You need to drop rows containing any missing data (NaNs). Which function do you use?**
A) `df.drop_nulls()`
B) `df.fillna(0)`
C) `df.dropna()`
D) `df.remove_nan()`

**4. True or False: `df.apply()` is highly optimized in C and should be used instead of vectorization for performance.**
A) True
B) False

**5. What does the `axis=1` parameter generally refer to in Pandas operations (like `.drop('col', axis=1)`)?**
A) Rows
B) Columns
C) The entire DataFrame
D) The Index

---
### Answers
1. **B** (Series = 1 column, DataFrame = tabular structure).
2. **C** (`describe()` generates descriptive statistics).
3. **C** (`dropna()` removes missing values).
4. **False** (`apply()` acts as a slow Python `for` loop under the hood. Avoid it for massive datasets).
5. **B** (Axis 0 is rows/index, Axis 1 is columns).
