import pandas as pd

# Series – jak kolumna w Excelu
s = pd.Series([10, 20, 30], name="Liczby")

# DataFrame – jak tabela
data = {
    "Imię": ["Anna", "Jan", "Kasia"],
    "Wiek": [23, 35, 29],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk"]
}
df = pd.DataFrame(data)

print(s)

print('\nteraz data frame \n')

print(df)


#task, 

print('\nmultplle FX for  USD/PLN from the last 5 days\n')



s1=pd.Series([3.6512,3.6248,3.6414,3.6679,3.6777], name='FX for USD/PLN')
print(s1)

data1 = {
    "FX": ["USDPLN", "USDPLN", "USDPLN"],
    "Rate": [3.6512, 3.6648, 3.6614],
    "Day": ["08-Sep-2025", "09-Sep-2025", "10-Sep-2025"]
}

df1=pd.DataFrame(data1)

df1["Day"]=pd.to_datetime(df1["Day"], format="%d-%b-%Y")


# 🔹 Jak działa format?
# %d → dzień (01–31)
# %b → skrót nazwy miesiąca (Jan, Feb, Mar, …)
# %B → pełna nazwa miesiąca (January, February, …)
# %Y → rok czterocyfrowy

print(df1)

print('\n multplle FX for  USD/PLN from the last 3 days as DataFrame \n')

print(df1[["FX","Rate"]]) # show only two columns out of three

print(df1[df1["Rate"]>3.66]) # show all columns but the rows are filtered

print('\n print only first row \n')

print(df1.iloc[0])  # iloc , index location by integer position

# wybiera dane po numerze wiersza / kolumny (czyli po pozycji w tabeli),

# myślisz o tym jak o zwykłym indeksie listy w Pythonie.


# df.iloc[0]      # pierwszy wiersz (index 0)
# df.iloc[0, 1]   # element z pierwszego wiersza i drugiej kolumny
# df.iloc[0:2]    # pierwsze dwa wiersze


print('\n print only first row \n')

print(df1.loc[0,"Rate"]) # lcoation by label

# wybiera dane po etykiecie indeksu lub nazwie kolumny,

# bardziej „czytelne”, bo odwołujesz się po nazwach.

# 👉 przykład:

# df.loc[0, "Imię"]        # Imię z wiersza o indeksie 0
# df.loc[0]                # cały wiersz o indeksie 0
# df.loc[:, "Imię"]        # wszystkie wiersze, kolumna "Imię"
# df.loc[0:1, ["Imię","Wiek"]]  # wycinek tabeli

print('\n  all rows , with column "RAte" \n')
print(df1.loc[:,"Rate"] ) # wszystkie wiersze, kolumna "Imię"
