# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.array([3000, 800, 600, 500, 520, 550, 700, 800, 1000, 650, 550, 750, 1100, 1200, 1500, 1900, 2000, 2500, 1300, 1200, 1200])
print(X)
Y = np.array([0, 25, 50, 0, 20, 75, 200, 500, 700, 1600, 750, 600, 400, 300, 200, 0, 0, 0, 750, 300, 0])
print(Y)

Z = np.array([0.9567, 0.02, 0.02, 0, 0, 0, 0.02, 0, 0, 0, 0, 0, 0.492, 0.02, 0.97667, 0.5, 1, 1, 0.02, 0.97667, 0.02])

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Creating plot
ax.scatter3D(X, Y, Z, color="blue")
plt.title("simple 3D scatter plot")
ax.set_xlabel('distance')
ax.set_ylabel('Human Velocity')
ax.set_zlabel('k value')
# show plot
plt.show()