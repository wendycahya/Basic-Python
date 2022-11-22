from simpful import *
import matplotlib.pylab as plt
from numpy import linspace, array
# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(function=Sigmoid_MF(c=300, a=0.05), term="positive")
S_2 = FuzzySet(function=InvSigmoid_MF(c=300, a=0.05), term="negative")
input1 = LinguisticVariable([S_1, S_2], concept="Derivative Distance", universe_of_discourse=[0, 600])
FS.add_linguistic_variable("TimeDistance", input1)
input1.plot()

F_1 = FuzzySet(function=Sigmoid_MF(c=300, a=0.05), term="positive")
F_2 = FuzzySet(function=InvSigmoid_MF(c=300, a=0.05), term="negative")
input2 = LinguisticVariable([F_1, F_2], concept="Scalar Product", universe_of_discourse=[0, 600])
FS.add_linguistic_variable("ScalarProduct", input2)
input2.plot()

T_1 = FuzzySet(function=Sigmoid_MF(c=0.6, a=40), term="high")
T_2 = FuzzySet(function=Gaussian_MF(mu=0.5, sigma=0.1), term="medium")
T_3 = FuzzySet(function=InvSigmoid_MF(c=0.4, a=40), term="small")
target = LinguisticVariable([T_1, T_2, T_3], concept="Alpha", universe_of_discourse=[0, 1])
FS.add_linguistic_variable("AlphaValue", target)
target.plot()
#
# # Define fuzzy rules
R1 = "IF (TimeDistance IS negative) OR (ScalarProduct IS positive) THEN (AlphaValue IS high)"
R2 = "IF (TimeDistance IS negative) OR (ScalarProduct IS negative) THEN (AlphaValue IS high)"
R3 = "IF (TimeDistance IS positive) OR (ScalarProduct IS negative) THEN (AlphaValue IS small)"
R4 = "IF (TimeDistance IS positive) OR (ScalarProduct IS positive) THEN (AlphaValue IS medium)"

FS.add_rules([R1, R2, R3, R4])
#
# # Set antecedents values
FS.set_variable("TimeDistance", 450)
FS.set_variable("ScalarProduct", 600)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["AlphaValue"]))

# Plotting surface
xs = []
ys = []
zs = []
DIVs = 50
for x in linspace(0, 600, DIVs):
    for y in linspace(0, 600, DIVs):
        FS.set_variable("TimeDistance", x)
        FS.set_variable("ScalarProduct", y)
        tip = FS.inference()['AlphaValue']
        xs.append(x)
        ys.append(y)
        zs.append(tip)
xs = array(xs)
ys = array(ys)
zs = array(zs)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xx, yy = plt.meshgrid(xs, ys)

ax.plot_trisurf(xs, ys, zs, vmin=0, vmax=1, cmap='gnuplot2')
ax.set_xlabel("Time Distance")
ax.set_ylabel("Scalar Product")
ax.set_zlabel("Alpha Product")
ax.set_title("Human Robot Collaboration", pad=50)
ax.set_zlim(0, 1)
plt.tight_layout()
plt.show()