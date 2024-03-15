'''Дан кортеж и элемент Х. Создать новый кортеж, начинающийся с первого
появления элемента Х в нем и заканчивающийся вторым его появлением
включительно.
Если элемента нет – создать пустой кортеж. Если элемент встречается только
один раз, то создать кортеж, который начинается с него и идет до конца
исходного.
Пример: кортеж=(1, 8, 3, 4, 8, 8, 9, 2), Х=8
получили (8, 3, 4, 8)'''

def get_tuple_with_x(t: tuple, x) -> tuple:
    if x not in t:
        return ()
    if t.count(x) == 1:
        return t[t.index(x):]
    first_index = t.index(x)
    second_index = t.index(x, first_index + 1)
    return t[first_index:second_index + 1]

t = tuple(map(int, input("Введите кортеж через запятую: ").split(",")))
x = int(input("Введите элемент x: "))
print(get_tuple_with_x(t, x))