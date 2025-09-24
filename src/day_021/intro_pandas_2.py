import pandas as pd

sales = pd.DataFrame({
    "Miasto": ["Warszawa", "Warszawa", "Kraków", "Gdańsk", "Kraków"],
    "Sprzedaż": [200, 150, 300, 250, 400]
})

print('Średnia sprzedaż w każdym mieście')
print(sales.groupby("Miasto")["Sprzedaż"].mean())

# Pivot table
print(sales.pivot_table(values="Sprzedaż", index="Miasto", aggfunc="sum"))




dirty = pd.DataFrame({
    "Imię": ["Anna", "Jan", "Jan", None],
    "Wiek": [23, None, 35, 40]
})

print(dirty)


# print('Usuwanie braków')
# print(dirty.dropna())

print(dirty.groupby("Imię")["Wiek"].mean())

print('zastapienie brakow srednia')
# print(dirty["Wiek"].fillna(dirty["Wiek"].mean(), inplace=True))

dirty["Wiek"]=dirty["Wiek"].fillna(dirty["Wiek"].mean())

# print(dirty["Wiek"])
print(dirty)

print('MEtoda groupby: \n')
print(dirty.groupby("Imię")["Wiek"].mean())





# 'df[col].method(value, inplace=True)'


# df[col] = df[col].method(value)