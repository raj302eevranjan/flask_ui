import numpy as np
from matplotlib import pyplot as plt

arr = np.load('bengin_normal_malignant.npy')
plt.plot(arr)
plt.title("Accuracy graph for tumour type")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.show()