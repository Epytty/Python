'''Дано уравнение 5x 3 -x 2 −20x+4, найти корни. Выполнить обратную операцию (зная
список корней, получить коэффициенты уравнения)'''
import numpy as np

coefficients = [5, -1, -20, 4]
roots = np.roots(coefficients)

print("Корни уравнения:", roots)
roots = [-1, 0.8+1.2j, 0.8-1.2j]
coefficients = np.poly(roots)

print("Коэффициенты уравнения:", coefficients)

coefficients1 = [3, 6, -9, 0, 0]
roots1 = np.roots(coefficients1)

print("Корни уравнения 2:", roots1)

roots1 = [0, 1, -1.41421356]
coefficients1 = np.poly(roots1)

print("Коэффициенты уравнения:", coefficients1)