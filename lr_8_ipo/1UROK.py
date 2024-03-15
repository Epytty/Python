import pandas as pd
dict_city = {"City":['Moscow', 'Saint-Petersburg', 'Novosibirsk'],'Population': [12670879, 5398064,1625631]}
df =pd.DataFrame(dict_city)
print(df)
lists_city =[["Moscow",'Saint-Petersburg','Novosibirsk'],[12670879,5398064,1625631]]
print(pd.DataFrame(lists_city))
print(pd.DataFrame(lists_city).T)

df = pd.read_csv("IHME-GBD_2019_DATA-ff08d9bc-1.csv", encoding = "utf-8")
print(df.head())

print(df.head(8))

print(df.tail())

print(df.info())

print(df.shape)

print(df.describe())

print(df.describe(include = 'all'))

print(df.dropna(inplace=True))

print(df['measure'])

print(df.measure)

print(df[['location', 'sex', 'year']])

print(df.loc[:,'location':'val'])

print(df.loc[100:100,'location':'val'])

print(df.iloc[100:100, 0:3])

print(df[df["sex"] == "Both"])

print(df[(df["sex"] == "Both") & (df["cause"] == "Cardiovascular diseases") & (df["year"] == 2019)])

print(df[(df["sex"] == "Both") & (df["cause"] == "Cardiovascular diseases") & (df["year"] == 2019) & (df["val"] > 600)])

cardio = df[(df["sex"] == "Both")&(df["cause"] == "Cardiovascular diseases") & (df["year"] == 2019) & (df["val"] > 600)]
print(cardio)

print(cardio.sort_values(by = ["val"], ascending=False, inplace=False, na_position='last', ignore_index=False))

print(df[(df["location"] == "Russia") | (df["location"] == "Russian Federation")])

print(df[df["cause"].str.contains("HIV")])

print(df[df["cause"].str.contains("HIV") == False])

print(df[~df["cause"].str.contains("HIV")])

print(df.drop("measure", axis=1, inplace = True))

df.drop(["metric","age","upper","lower"], axis=1, inplace = True)
print(df)

df["val_round"] = df["val"].round(decimals = 1)
print(df.head())

df.rename(columns = {"val": "value"}, inplace = True)
print(df)