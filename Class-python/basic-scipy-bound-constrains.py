#Ref: https://pythonguides.com/scipy-optimize/
# https://pythonguides.com/python-scipy-linprog/

# Importing the linprog
from scipy.optimize import linprog

# defining Coefficient for x and y
objective = [-1, -3]

# defining Coefficient inequalities
lhs_inequality = [[ 3,  1],
           [-5,  6],
           [ 1, -3]]

rhs_inequality = [25,
            15,
              3]

lhs_equality = [[-1, 6]]
rhs_equality = [20]

# defining the bounds for each variable
bound = [(0, float("inf")),  # bounds of x
     (0, float("inf"))]  # bounds of y

# Optimizing the problems using the method linprog()
opt_res = linprog(c=objective, A_ub=lhs_inequality, b_ub=rhs_inequality, A_eq=lhs_equality, b_eq=rhs_equality, bounds=bound, method="revised simplex")

print(opt_res)