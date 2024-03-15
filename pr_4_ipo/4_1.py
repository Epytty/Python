'''В файле в столбик записаны целые числа. Напишите программу, которая определяет длину самой длинной цепочки идущих подряд одинаковых чисел, записанных в файле в столбик, и выводит результат в другой файл. Учтите, что таких цепочек может вообще не быть..'''

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

max_length = 0
current_length = 1

for i in range(1, len(data)):
    if data[i] == data[i-1]:
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 1

max_length = max(max_length, current_length)

with open('output.txt', 'w') as f:
    f.write(str(max_length))