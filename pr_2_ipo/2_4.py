'''Дано число n. Создайте массив размером n×n и заполните его по
следующему правилу: случайные числа от 1 до 9, все элементы
главной диагонали замените на 0, все числа больше 7 замените на
отрицательные. Исходный и полученный массивы выведите на экран.
Числа в строке разделяйте одним пробелом.'''

import random
n=int(input('Введите размер матрицы NxN: '))
arr = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 9))
    arr.append(row)
print("Исходный массив:")
for row in arr:
    print(" ".join(str(elem) for elem in row))
for i in range(n):
    arr[i][i] = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > 7:
            arr[i][j] = -arr[i][j]
print("Полученный массив:")
for row in arr:
    print(" ".join(str(elem) for elem in row))