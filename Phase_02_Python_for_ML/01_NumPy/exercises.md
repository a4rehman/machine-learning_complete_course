# Exercises: NumPy Mastery

### Beginner Problems

**Exercise 1: Array Creation**
Create a 1D NumPy array containing the numbers from 10 to 49. Then, reverse the array so it goes from 49 to 10.

**Exercise 2: Reshaping**
Create a 1D array of 9 elements (from 0 to 8). Reshape it into a 3x3 matrix.

---

### Intermediate Problems

**Exercise 3: Standardization (Math to Code)**
In Machine Learning, we often "Standardize" our data so it has a mean of 0 and standard deviation of 1.
Given a random 1D array of 50 numbers: `data = np.random.randn(50) * 10 + 5`
Write a one-liner using NumPy to subtract the mean of `data` and divide by the standard deviation of `data`.

**Exercise 4: Boolean Extraction**
Given a 2D array `matrix = np.random.randint(1, 100, size=(5,5))`:
1. Find all values greater than 50.
2. Replace all values less than 20 with the number `0`. (Hint: use `np.where`).

---

### Advanced Problems

**Exercise 5: Dot Product (Neural Network Basics)**
A basic neural network neuron performs a dot product between Inputs and Weights, and adds a Bias.
```python
inputs = np.array([[1.0, 2.0, 3.0], [2.5, 3.1, -1.2]]) # Batch of 2 inputs, 3 features each
weights = np.array([0.2, 0.8, -0.5]) # 3 weights
bias = 2.0
```
Write the NumPy code to calculate the output for this batch. (Hint: Use `np.dot` or the `@` operator).

**Exercise 6: Real-world image simulation**
An RGB image is a 3D array of shape `(Height, Width, 3)`.
Create a dummy image array of shape `(256, 256, 3)` filled with random integers from 0 to 255.
Convert this color image to grayscale by taking the mean across the color channel (axis 2). The resulting shape should be `(256, 256)`.
