'''Используя данные задания 2, выполнить подсчет выживших относительно класса
каюты.'''
import pandas as pd

df = pd.r('titanic.csv')
s = df.groupby(['PClass', 'Survived']).size().reset_index(name='count')
print(s)