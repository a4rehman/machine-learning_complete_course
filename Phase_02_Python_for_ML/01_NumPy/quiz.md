# Quiz: NumPy for ML

**1. What is the primary reason NumPy is faster than Python lists?**
A) It uses multi-threading by default.
B) It stores data in contiguous blocks of memory and uses C-compiled code.
C) It compresses the data to save RAM.
D) It relies on cloud computing.

**2. If you have an array `A` of shape (4, 3) and array `B` of shape (3,), what will the shape of `A + B` be due to broadcasting?**
A) (4, 3)
B) (3, 4)
C) Error: Shapes do not match.
D) (12,)

**3. Which NumPy function is best for replacing values based on a condition without writing a loop?**
A) `np.replace()`
B) `np.loop()`
C) `np.where()`
D) `np.apply()`

**4. What is the shape of `np.zeros((2, 3, 4))`?**
A) 2 rows, 12 columns
B) A 3D array with 2 blocks, 3 rows, and 4 columns.
C) 24 elements in a 1D array.
D) Error.

**5. True or False: A NumPy array can comfortably hold strings, integers, and floats in the exact same array without converting them to a common string type.**
A) True
B) False

---
### Answers
1. **B** (Contiguous memory and C optimization prevent cache misses).
2. **A** (Broadcasting duplicates the 1D array across all 4 rows).
3. **C** (`np.where(condition, value_if_true, value_if_false)`).
4. **B** (It creates a 3-dimensional tensor).
5. **False** (NumPy arrays are homogeneous; mixing types forces everything to strings/objects, killing performance).
