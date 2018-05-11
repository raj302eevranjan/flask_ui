import numpy as np
from matplotlib import pyplot as plt

arr = np.load('7stages.npy')
plt.plot(arr)
plt.title("accuracy for 7 stage")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.show()