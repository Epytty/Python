'''Определить средние значения по всем строкам и столбцам матрицы.
Результат оформить в виде матрицы из N + 1 строк и M + 1 столбцов.'''

import random
N =int(input('Введите кол-во строк матрицы: '))
M =int(input('Введите кол-во столбцов матрицы: '))
matrix = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(random.randint(1, 10))
    matrix.append(row)
print("Исходная матрица:")

for row in matrix:
    print(row)
new_matrix = []
for i in range(N+1):
    row = []
    for j in range(M+1):
        row.append(0)
    new_matrix.append(row)

for i in range(N):
    row_sum = 0
    for j in range(M):
        row_sum += matrix[i][j]
        new_matrix[i][j] = matrix[i][j]
    row_avg = row_sum / M
    new_matrix[i][M] = row_avg

for j in range(M):
    col_sum = 0
    for i in range(N):
        col_sum += matrix[i][j]
    col_avg = col_sum / N
    new_matrix[N][j] = col_avg

matrix_sum = 0
for row in matrix:
    for elem in row:
        matrix_sum += elem
matrix_avg = matrix_sum / (N * M)
new_matrix[N][M] = matrix_avg

print("Матрица со средними значениями:")
for row in new_matrix:
    print(row)