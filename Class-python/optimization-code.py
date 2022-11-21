# Using CVXPY
import cvxpy as cp

pp = cp.Variable()
pc = cp.Variable()

qp = cp.Variable()
qc = cp.Variable()

pfr = cp.Variable()
pto = cp.Variable()

qfr = cp.Variable()
qto = cp.Variable()

constraints = [pp >= 0, pc >= 0, pc <= 100,
               pfr >= 0, qfr >= 0,
               pto >= 0, qto >= 0,
               pfr ** 2 + qfr ** 2 <= 12,
               pto ** 2 + qto ** 2 <= 24,
               pp == pc + pfr + pto,
               qp == qc + qfr + qto

               ]
prob = cp.Problem(cp.Maximize(5 * pc - 4 * pp), constraints)

prob.solve()

# Print result.
print("The optimal value is", prob.value)
print("A solution x is")
print(pp.value)
print(pc.value)