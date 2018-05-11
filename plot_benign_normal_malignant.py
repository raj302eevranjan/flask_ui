import numpy as np
from matplotlib import pyplot as plt

arr = np.load('plot_benign_normal_malignant.npy')
plt.plot(arr)
plt.show()