# 5. Łączenie danych

# Merge, Join, Concat

import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3], "Imię": ["Anna", "Jan", "Kasia"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "Wiek": [23, 35, 29]})


print(df1)

print(df2)

df3_merged=pd.merge(df1,df2,on='ID')
print(df3_merged)


df4=pd.DataFrame({"ID":[4,5], 'Imie':['Ola','Tomek']})
concat=pd.concat([df3_merged,df4],ignore_index=True)

print(concat)