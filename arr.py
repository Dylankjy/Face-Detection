import numpy as np
import matplotlib.pyplot as plt

# Black and white image
bw_arr = np.array([
    [0, 0, 0],
    [100, 100, 100],
    [255, 255, 255]
])

plt.imshow(bw_arr, cmap="gray")  # Need to specify cmap because default isn't greyscale
plt.show()

# Red, Green, Blue Array
rgb_arr = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 0], [0, 0, 255]]
])

plt.imshow(rgb_arr)
plt.show()
