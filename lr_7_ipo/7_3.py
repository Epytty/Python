
import numpy as np

A = np.array([[3, -3, -5, 8], [-3, 2, 4, -6], [2,-5, -7, 5], [-4, 3, 4, -6]])
det_A = np.linalg.det(A)
B = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
det_B = np.linalg.det(B)
print("Определитель матрицы A равен:", det_A)
print("Определитель матрицы A равен:", det_B)