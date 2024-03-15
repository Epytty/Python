import pandas as pd  # загрузка библиотеки pandas

df = pd.read_csv(r"IHME-GBD_2019_DATA-ff08d9bc-1.csv", delimiter=',', encoding='utf-8')
print(df.head())  # первые 5 строк датафрейма
print(df.shape)  # число строк и столбцов в датафрейме
print(df.columns)  # названия столбцов
print(df.describe())  # статистика по числовым столбцам

print(df["val"].mean())  # среднее по одному столбцу
print(df['val'].max())  # максимальное значение по одному столбцу
print(df['val'].min())  # минимальное значение по одному столбцу
print(df['cause'].count())  # число записей
print(df['cause'].unique())  # уникальные значения

df['cause'].value_counts() # число записей соответствующих уникальным значениям

df.sort_values(['val'], ascending = False) # сортировка

df.nlargest(5,'val') # 5 наибольших значений по столбцу 'val'

df[df['year'] == 2019].nlargest(5,'val') # 5 наибольших значений по столбцу 'val' для 2019 года

df[(df['location'].isin(['Russian Federation', 'Ukraine', 'Belarus'])) & (df['year'] == 2019)].nlargest(5,'val')
# 5 наибольших значений по столбцу 'val' для 2019 года для стран Россия, Украина и Беларуси

df.nsmallest(7, 'val') # 7 минимальных значений 'val'

# среднее значение по всем числовым столбцам для каждой причины смерти

df_cause = df.groupby('cause').agg({'year': ['count'], 'val': ['mean', 'median']})
# статистика по причинам смерти
# для столбца year считаем count (число уникальных значений), для 'val' — среднее и медиану
print(df_cause)


df_cause.index # индексы — причины смерти


df_cause.index # индексы — причины смерти


df_cause.index # индексы — причины смерти

df_gender = df.groupby(['cause', 'sex']).agg({'val': ['mean', 'median']})
df_gender


df_gender.xs('Transport injuries', level = 'cause') #  выбор по мультииндексу

df_gender.xs('Transport injuries', level = 'cause')['val'].loc["Male",'median']
# выбор значения по мутьтииндексу + метод loc

df_pivot = df.pivot_table(values='val', index='location', columns='cause', aggfunc='mean',
                      margins=False, dropna=True, fill_value=None) # сводная таблица
df_pivot

df_pivot = df.pivot_table(values='val', index='location', columns='cause', aggfunc='mean',
                      margins=True, dropna=True, fill_value=None)
# добавляем поля All (обобщенное значение по всем строкам и столбцам) с помощью Margins = True
df_pivot

df_pivot = df.pivot_table(values='val', index='location', columns='cause', aggfunc='mean',
                      margins=False, dropna=True, fill_value=None)
df_pivot

df_pivot.index


df_pivot.columns

df_pivot.loc['Russian Federation', 'HIV/AIDS and sexually transmitted infections'] # выбор значений в сводной таблице

df_pivot = df.pivot_table(values='val', index='year', columns='cause', aggfunc='mean',
                      margins=False, dropna=True, fill_value=None) # в качестве индексов берем годы
df_pivot


df_pivot = df.pivot_table(values='val', index=['location','year'], columns='cause', aggfunc='mean',
                      margins=False, dropna=True, fill_value=None)
# задаем мультииндекс (страны и годы)


df_pivot

df_pivot.loc['Russian Federation','HIV/AIDS and sexually transmitted infections']


