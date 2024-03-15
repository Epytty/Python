import numpy as np

n = 5
m = 4
k = -5

mat = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        mat[i][j] = k + j

print(mat)
print()
n1 = 5
m1 = 4
k1 = -5

mat1 = np.zeros((n, m))
for i in range(m):
    for j in range(n):
        mat1[j][i] = k + j

print(mat1)