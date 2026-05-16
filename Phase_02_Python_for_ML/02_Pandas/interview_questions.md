# Interview Questions: Pandas

### 🟢 Beginner Level

**Q1: How do you check for missing values in a Pandas DataFrame?**
**Answer:** `df.isnull().sum()` or `df.isna().sum()`. This creates a boolean mask of the DataFrame and sums the `True` values column by column, returning the count of missing values per feature.

**Q2: What is the difference between `.merge()` and `.concat()`?**
**Answer:** `.merge()` is used to combine DataFrames based on common columns or indices (similar to SQL JOINs like Inner, Left, Right). `.concat()` is used to "glue" DataFrames together either vertically (stacking rows) or horizontally (adding columns side-by-side) without necessarily matching keys.

### 🟡 Intermediate Level

**Q3: How would you handle a highly imbalanced categorical column containing 100 unique categories before feeding it to an ML model?**
**Answer:** Feeding 100 unique categories to `pd.get_dummies()` (One-Hot Encoding) would create 100 new columns, causing the "Curse of Dimensionality" and slowing down the model. Instead, I would look at the frequency of categories. I'd keep the top 10 most frequent categories, and group the remaining 90 rare categories into a single new category called "Other".

**Q4: Explain how Pandas `.groupby()` works under the hood.**
**Answer:** It follows the "Split-Apply-Combine" paradigm. First, it **splits** the data into distinct groups based on the key(s) provided. Second, it **applies** an aggregation function (like mean, sum, or a custom lambda) to each group independently. Finally, it **combines** the results back into a single structured DataFrame.

### 🔴 FAANG Level (Data Engineering)

**Q5: You need to process a 50 GB CSV file using Pandas, but your EC2 instance only has 16 GB of RAM. `pd.read_csv()` throws an OutOfMemory (OOM) error. How do you solve this?**
**Answer:** Pandas loads the entire dataset into memory at once. To fix this, I can:
1. Use the `chunksize` parameter in `pd.read_csv(chunksize=100000)` which returns an iterator. I can process the data chunk-by-chunk and save aggregated results.
2. Only load the specific columns I need using the `usecols` parameter.
3. Change default data types to save memory (e.g., loading `int64` as `int32`, or strings as `category`).
4. Better yet, bypass Pandas completely and use a distributed framework like **PySpark** or a lazy-evaluation library like **Polars** or **Dask** which are designed for out-of-core computation.
