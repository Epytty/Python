'''Дано целое число N (&gt; 1) и набор из N целых чисел. Вывести те элементы
в наборе, которые меньше своего левого соседа, и количество K таких
элементов.'''

n=int(input('Введите кол-во элементов: '))
print('Введите',n,'целых чисел: ')
a=[]
for i in range(n):
    a.append(int(input()))
print('Полученный список:',a)
k=[]
for i in range(n):
    if (i<n-1) and a[i] > a[i+1]:
        k.append(a[i+1])
print(k)
print('Элементов, которые меньше своего левого соседа:', len(k))