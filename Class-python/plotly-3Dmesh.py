# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.array([3000, 800, 600, 500, 520, 550, 700, 800, 1000, 650, 550, 750, 1100, 1200, 1500, 1900, 2000, 2500, 1300, 1200, 1200, 1200, 1200, 1300, 1400, 1500, 1700, 1800, 2100, 2700, 2750, 2800, 2800, 2800, 2800, 2600, 2400, 2200, 2100, 1850, 1700, 1600, 1400, 1320, 1289, 1240, 1150, 1000, 820, 614, 512, 2500])
print(X)
Y = np.array([0, 25, 50, 0, 20, 75, 200, 500, 700, 1600, 750, 600, 400, 300, 200, 0, 0, 0, 750, 300, 0, 0, 0, 130, 110, 151, 120, 140, 168, 50, 100, 0, 0, 0, 0, 180, 120, 126, 156, 421, 230, 253, 267, 218, 289, 389, 318, 198, 169, 129, 290, 1600])
print(Y)
Z = np.array([0.9567, 0.02, 0.02, 0, 0, 0, 0.02, 0, 0, 0, 0, 0, 0.492, 0.02, 0.97667, 0.5, 1, 1, 0.02, 0.97667, 0.02, 0.02, 0.97667, 0.02, 0.97667, 0.02, 0.97667, 0.02, 0.97667, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0.02, 0.97667, 0.02, 0.97667, 0.02, 0.97667, 0.02, 0.02, 0.02, 0, 0, 0.95667])

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Creating plot
ax.scatter3D(X, Y, Z, color="blue")
plt.title("Human Distance, Human Velocity, and k-value Comparison")
ax.set_xlabel('distance')
ax.set_ylabel('Human Velocity')
ax.set_zlabel('k value')
# show plot
plt.show()