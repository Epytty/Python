'''Составьте блок-схему поиска максимального элемента
в одномерном массиве и напишите соответствующую программу, не используя
встроенных методов.
Задача поиска максимального элемента в массиве решается следующим
образом. Пусть maxA — требуемое значение максимального элемента. Сначала
присваиваем переменной maxA значение первого элемента массива, потом
сравниваем первый элемент со следующим. Если следующий элемент (второй) больше
первого, присваиваем его значение переменной maxA, а если нет — переходим к
следующему (третьему элементу) и т. д.
Аналогично решается задача поиска минимального элемента в массиве. В
Python эти алгоритмы уже реализованы в функциях max(), min() и в методе sort ()
(метод sort () сортирует список по возрастанию значений элементов).'''

import random
n=int(input('Введите количество элементов в массиве: '))
a=[random.randint(-100,100) for i in range(n)]
maxA=a[0]
for i in range(n):
    if a[i]>maxA:
        a[i]=maxA
print(a)
print(maxA)