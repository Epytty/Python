import numpy as np

def round_array(A):
    return np.where(A > 0, np.ceil(A), np.floor(A))

A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
print(round_array(A))