'''Поместите данный код в отдельный файл square.py.
Когда интерпретатор Python встречает команду импорта, то просматривает на
наличие файла-модуля определенные каталоги. Если вы сохраните файл-модуль и
файл-программу в одном каталоге, то интерпретатор без труда найдет модуль.
Поместите файл square.py в тот же каталог, где будет исполняемая
программа. Ее код должен включать инструкцию импорта модуля square (при
импорте расширение файла не указывается) и вызов той функции и с теми
параметрами, которые ввел пользователь. Т. е. у пользователя надо спросить,
площадь какой фигуры он хочет вычислить. Далее запросить у него аргументы для
соответствующей функции. Передать их в функцию из модуля square, а
полученный оттуда результат вывести на экран.'''

import square
f=str(input('Введите площадь какой фигуры (прямоугольник, треугольник, круг) вы хотите вычислить: '))
try:
    if f == 'Прямоугольник':
        a=int(input('Введите длинну стороны а прямоугольника: '))
        b=int(input('Введите длинну стороны b прямоугольника: '))
        print('Площадь прямоугольника равна: ',square.rectangle(a,b))
    elif f == 'Треугольник':
        a=int(input('Введите длинну стороны а треугольника: '))
        h=int(input('Введите длинну высоты треугольника: '))
        print('Площадь треугольника равна: ',square.triangle(a,h))
    elif f == 'Круг':
        r=int(input('Введите длинну радиуса круга: '))
        print('Площадь круга равна: ',square.circle(r))
except:
    print('Неверный ввод')