import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

#ax = plt.subplot(111)
#ax.imshow(data[0], data[1])


ax = plt.subplot(111)
im = ax.imshow(np.arange(100).reshape((10, 10)))

plt.show()