import numpy as np
from matplotlib import pyplot as plt

arr = np.load('plot_fat_dense_glandular.npy')
plt.plot(arr)
plt.show()