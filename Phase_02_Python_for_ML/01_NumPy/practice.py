"""
Phase 02: Python for ML
Topic: 01 - NumPy Basics to Advanced
"""

import numpy as np
import time

# ==============================================================================
# 1. BEGINNER: Creating Arrays and Basics
# ==============================================================================
print("--- BEGINNER: Array Creation ---")

# 1D Array (Vector)
vector = np.array([1, 2, 3, 4, 5])
print(f"Vector shape: {vector.shape}, dimensions: {vector.ndim}")

# 2D Array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix shape: {matrix.shape}, dimensions: {matrix.ndim}")

# Special Arrays
zeros = np.zeros((3, 3))        # 3x3 matrix of zeros
ones = np.ones((2, 4))          # 2x4 matrix of ones
random_arr = np.random.rand(2, 2) # Random values between 0 and 1
print(f"Random Array:\n{random_arr}\n")


# ==============================================================================
# 2. INTERMEDIATE: Indexing, Slicing & Filtering
# ==============================================================================
print("--- INTERMEDIATE: Slicing & Filtering ---")

data = np.arange(1, 17).reshape(4, 4) # 4x4 matrix from 1 to 16
print(f"Original Data:\n{data}")

# Get the first 2 rows and last 2 columns
slice_data = data[:2, 2:] 
print(f"Sliced Data:\n{slice_data}")

# Boolean Indexing (Filtering) - Very common in ML
# e.g., Filter out all values less than 10
filtered = data[data > 10]
print(f"Values > 10: {filtered}\n")


# ==============================================================================
# 3. ADVANCED: Vectorization & Broadcasting
# ==============================================================================
print("--- ADVANCED: Vectorization Speed Test ---")

# Comparing Python loops vs NumPy Vectorization
size = 10_000_000
list_a = list(range(size))
list_b = list(range(size))

arr_a = np.arange(size)
arr_b = np.arange(size)

# Python Loop Timing
start = time.time()
list_c = [list_a[i] + list_b[i] for i in range(size)]
python_time = time.time() - start

# NumPy Vectorized Timing
start = time.time()
arr_c = arr_a + arr_b
numpy_time = time.time() - start

print(f"Python Loop Time: {python_time:.4f} seconds")
print(f"NumPy Vector Time: {numpy_time:.4f} seconds")
print(f"NumPy is {python_time / numpy_time:.2f}x faster!\n")

print("--- Broadcasting Example ---")
# Adding a 1D array to a 2D array without matching shapes!
matrix = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3
vector = np.array([10, 20, 30])           # 1x3
print(f"Broadcast Result:\n{matrix + vector}") 
# NumPy automatically 'broadcasts' the vector across all rows of the matrix.
