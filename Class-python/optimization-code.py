# Using CVXPY
import cvxpy as cp
import numpy as np

A = np.array([[0, -1, 0, -1, 1, 0],
              [-2, 1, 0, 2, 0, -1],
              [0, 1, 0, 0, 0, 1],
              [0, 0, 1, 0, -1, 2]
              ])
b = np.array([2, 1, 1, -3])

x_L1 = cp.Variable(shape=6)

constraints = [A*x_L1 == b]

obj = cp.Minimize(cp.norm(x_L1, 1))

prob = cp.Problem(obj, constraints)
prob.solve()

print("Status: {}".format(prob.status))

print("optimal objective value: {}".format(obj.value))

