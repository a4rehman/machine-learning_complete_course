# Interview Questions: NumPy

### 🟢 Beginner Level

**Q1: What is the difference between a Python List and a NumPy Array?**
**Answer:** Python lists are arrays of pointers to objects scattered in memory, which allows them to hold mixed data types but makes them slow. NumPy arrays are contiguous blocks of homogeneous data (all same type) in memory, making them cache-friendly and extremely fast for mathematical operations.

**Q2: What is vectorization?**
**Answer:** Vectorization is the process of applying an operation to an entire array at once rather than using an explicit `for` loop in Python. It pushes the loop down into optimized C code.

### 🟡 Intermediate Level

**Q3: Explain Broadcasting in NumPy.**
**Answer:** Broadcasting is a set of rules that allows NumPy to perform arithmetic operations on arrays of different shapes. For example, adding a scalar to an array, or adding a 1D array to a 2D matrix. NumPy logically "stretches" the smaller array across the larger one without actually copying the data in memory.

**Q4: How would you find the index of the maximum value in a 1D NumPy array?**
**Answer:** Using the `np.argmax(array)` function. This is heavily used in Deep Learning to find which class has the highest predicted probability (e.g., getting the final prediction from a softmax layer).

### 🔴 FAANG Level (System & Data Engineering)

**Q5: You have a NumPy array of size 50 GB, but your server only has 16 GB of RAM. How do you compute the mean of this array?**
**Answer:** You cannot load it into RAM using a standard `np.array()`. You have two options:
1. Use `np.memmap()` to map the array directly to a file on the hard drive, processing it in smaller chunks.
2. If it's a CSV/Parquet, read it in chunks (e.g., using Pandas `chunksize`), compute the sum and count for each chunk iteratively, and calculate the final mean at the end.
*(For highly distributed environments, migrating to PySpark or Dask is the industry standard).*
