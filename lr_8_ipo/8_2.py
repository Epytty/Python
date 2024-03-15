'''Используя набор данных о пассажирах Титаника
(https://disk.yandex.by/d/TfhJdE2k3EyALt), подсчитать с помощью метода .groupby(),
сколько женщин и мужчин выжило, а сколько нет.'''
import pandas as pd
df = pd.read_csv('titanic.csv')

s = df.groupby(['Sex', 'Survived'])['Survived'].count()
print(s)