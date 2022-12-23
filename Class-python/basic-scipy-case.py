import picos as pc

dPr = 10
dPrmax = 15
dPrmin = 0
ddPrmax = 15
ddPrmin = 0
dt = 0.5

Vr = 10
Vrmax = 25

dP_1 = 5

k = pc.RealVariable("k", 1) # Real variable x

problem = pc.Problem()

problem.minimize = -k # Objective
problem += k >= 0
problem += k <= 1
problem += dPr*k <= dPrmax
problem += -dPr*k <= -dPrmin
problem += (dPr/dt)*k <= ddPrmax + (dP_1/dt)
problem += -(dPr/dt)*k <= -ddPrmin + (dP_1/dt)

problem.solve(solver="cvxopt")

opt = problem.value

print("Optimal solution: %f (k = %f)" % (opt, k))