'''Каждый из некоторого множества студентов ВУЗа знает некоторое
количество языков. Нужно определить сколько языков знают все студенты, и
сколько языков знает хотя бы один из них. В первой строке задано
количество студентов. Для каждого из студентов сначала записано
количество языков, которое он знает, а затем - названия языков, по одному
в строке. В первой строке выведите количество языков, которые знают все
студенты. Начиная со второй строки - список таких языков. Затем -
количество языков, которые знает хотя бы один студент, на следующих
строках - список таких языков. Языки нужно выводить в
лексикографическом порядке, по одному на строке.'''

all_languages = set()
any_languages = set()
n = int(input('Введите кол-во студентов: '))
for i in range(n):
    m = int(input('Введите кол-во языков, которые он знает: '))
    student_languages = set()
    for j in range(m):
        language = input('Введите язык: ')
        student_languages.add(language)
        all_languages.add(language)
    if i == 0:
        any_languages = student_languages
    else:
        any_languages = any_languages.union(student_languages)
        any_languages = any_languages.intersection(student_languages)
print(len(any_languages))
for language in sorted(any_languages):
    print(language)
print(len(all_languages))
for language in sorted(all_languages):
    print(language)