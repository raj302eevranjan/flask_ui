import numpy as np
from matplotlib import pyplot as plt

arr = np.load('plot_fat_dense_glandular.npy')
plt.plot(arr)
plt.title("Accuracy graph for tumour type")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.show()