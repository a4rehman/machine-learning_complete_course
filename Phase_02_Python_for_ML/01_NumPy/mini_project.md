# Mini Project: Image Processing purely with NumPy

## Problem Statement
In Computer Vision, images are just 3D NumPy arrays (Height, Width, RGB Channels). Before using heavy libraries like OpenCV, you need to understand how to manipulate pixels mathematically. 

**Your Task**: Build a script that loads an image array, converts it to grayscale, and applies a basic edge-detection filter without using any image processing libraries.

## Dataset
You don't need to download an image. Generate a mock image:
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate a 100x100 RGB image with random noise
image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
```

## Step-by-Step Implementation

1. **Visualize the Original**: Use `plt.imshow(image)`.
2. **Grayscale Conversion**:
   The human eye is more sensitive to green. The standard formula for grayscale is:
   `Gray = (0.2989 * R) + (0.5870 * G) + (0.1140 * B)`
   Use NumPy slicing to extract the R, G, and B channels, apply the formula, and create a 2D array.
3. **Brightness Adjustment**: Add a scalar value of `50` to the entire grayscale array. Ensure you use `np.clip()` to keep values between 0 and 255.
4. **Display**: Use `plt.imshow(grayscale_image, cmap='gray')` to show your result.

## Expected Output
A deeper understanding of how Convolutional Neural Networks (CNNs) see and manipulate image data at the lowest memory level.
