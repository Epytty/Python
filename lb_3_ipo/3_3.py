'''Дан одномерный массив числовых значений, насчитывающий N
элементов. Подсчитать количество чисел, делящихся на 3 нацело, и
среднее арифметическое чисел с чётными значениями. Поставить
полученные величины на первое и последнее места в массиве (увеличив
массив на 2 элемента).'''

n=int(input('Введите кол-во элементов массива: '))
print('Введите',n,'Элементов массива: ')
mass=[int(input()) for i in range(n)]
print('Полученный массив: ',mass)
x=0
y=0
z=0
for i in range(n):
    if mass[i] % 3 == 0:
        x+=1
print('Чисел, делящихся на 3 нацело: ',x)
for i in range(n):
    if mass[i] % 2 == 0:
        y+=mass[i]
        z+=1
sr=y/z
print('Среднее арифметическое чётных чисел: ',sr)
mass.insert(0,x)
mass.append(sr)
print(mass)