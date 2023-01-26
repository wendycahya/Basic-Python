import picos as pc
import numpy as np
import math

#definition Tr, ac, C, Zd, Zr
# Vr turunan dari human and robot position dR, robot pos, human pos
# Vh turunan dari human and robot position dH, human pos, robot pos



def SSM_calculation(Vr, Vh, Tr, ac, C, Zd, Zr):
    Tb = Vr / ac
    Ss  = pow(Vr, 2) / (2*ac)
    Ctot = C + Zd + Zr
    Sp = Vh * ( Tr + Tb ) + (Vr * Tr) + Ss + Ctot
    return Sp

def inputVRVH(dIn, Pos1, Pos2):
    p1 = np.array(Pos1)
    p2 = np.array(Pos2)
    v1 = np.array(dIn)
    num = p2 - p1
    denum = np.linalg.norm(num)
    calcnumDenum = num/denum
    inputParam = abs(np.dot(v1, calcnumDenum))
    return inputParam

def velXYZ(Xn, Xn_last, ts):
    velX = (Xn_last[0] - Xn[0]) / ts
    velY = (Xn_last[1] - Xn[1]) / ts
    velZ = (Xn_last[2] - Xn[2]) / ts
    return velX, velY, velZ

#change variable
# xRob = 500
# yRob = 200
# zRob = 300
# XnRob = [xRob, yRob, zRob]
#
# xHum = 2200
# yHum = 200
# zHum = 300
# XnHum = [xHum, yHum, zHum]
#
# Xn_last = [xRob + 100, yRob, zRob]
#
# ts = 0.5
# d = math.dist(Xn_last, XnHum)

# VelnRob = velXYZ(XnRob, Xn_last, ts)
# Vr = inputVRVH(VelnRob, XnRob, XnHum)
dt = 0.41

d = 2200
SPmin = 515
Ssafe = 633
Scollab = 1911
SReduce = 3172.575

dPr = 1500
dP_1 = 0
Vr = 1500

Vrmax = 0
dPrmax = 1500
dPrmin = -1500
ddPrmax = 3500
ddPrmin = -3500


#constrains
if d > SReduce:
    Vrmax = 1500

elif d > Scollab and d <= SReduce:
    Vrmax = 2.7027*d - 4764.9

elif d <= Scollab and d > Ssafe:
    Vrmax = 400

elif d <= Ssafe and d > SPmin:
    Vrmax = 2.7027*d - 1391.9

elif d <= SPmin:
    Vrmax = 0


k = pc.RealVariable("k", 1) # Real variable x

problem = pc.Problem()

problem.minimize = -k # Objective
problem += k >= 0
problem += k <= 1
problem += k*Vr <= Vrmax
problem += dPr*k <= dPrmax
problem += -dPr*k <= -dPrmin
problem += (dPr/dt)*k <= ddPrmax + (dP_1/dt)
problem += -(dPr/dt)*k <= -ddPrmin + (dP_1/dt)

problem.solve(solver="cvxopt")

opt = problem.value



#print("distance HR: ", math.dist(Xn_last, XnHum))
print("Constraint Vrmax: ", Vrmax, " dPrmax: ", dPrmax)
print("Optimal solution: %f (k = %f)" % (opt, k))
print("Result: ", dPr*k)