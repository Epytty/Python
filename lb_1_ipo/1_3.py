'''Напишите программу, которая считывает целое число (например, 110) и выводит текст, аналогичный приведенному в примере (пробелы важны!):
The next number for the number 110 is 111.
The previous number for the number 110 is 109.'''

a=int(input())
print('The next number for the number', a,'is',a+1)
print('The previous number for the number', a,'is',a-1)
