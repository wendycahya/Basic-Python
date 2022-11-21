import numpy as np

def vel_SSM(vel1T, pos1, pos2):
    pos_compare = pos1 - pos2
    pos_abs = pos_compare / np.linalg.norm(pos_compare)
    print("Linalg norm:", np.linalg.norm(pos_compare))
    print(pos_abs)
    vel_input = abs(np.dot(vel1T, pos_abs))
    return vel_input


vel1 = np.array([[3], [2], [1],
        [0], [0], [0]])

vel1T = np.transpose(vel1)
pos1 = np.array([[1], [0], [0],
        [0], [0], [0]])
pos2 = np.array([[5], [0], [0],
        [0], [0], [0]])

vinput_SSM = vel_SSM(vel1T, pos1, pos2)
print(vinput_SSM)

