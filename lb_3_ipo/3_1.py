'''Написать программу, которая выполняет над двумя
вещественными числами одну из четырех арифметических операций (сложение,
вычитание, умножение или деление). Программа должна завершаться только по
желанию пользователя.'''

a=0
while a != 'Стоп':
    a=input('Введите одно из арифметических действий (слово "Стоп" останавливает программу): ')
    if a == '+':
        x=float(input('Введите первое число: '))
        y=float(input('Введите второе число: '))
        print('Сумма чисел равна:', x+y)
    elif a == '-':
        x=float(input('Введите первое число: '))
        y=float(input('Введите второе число: '))
        print('Вычитание чисел равна:', x-y)
    elif a == '/':
        x=float(input('Введите первое число: '))
        y=float(input('Введите второе число: '))
        if (x and y) == 0:
            print('Деление невозможно')
            continue
        else:
            print('Деление чисел равно:', x/y)
    elif a == '*':
        x=float(input('Введите первое число: '))
        y=float(input('Введите второе число: '))
        print('Произведение чисел равна:', x*y)
    elif a == 'Стоп':
        print('Программа остановлена')
        break
    elif a != '+' or '-' or '/' or '*' or 'Стоп':
        print('Неверный ввод')