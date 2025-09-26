import yfinance as yf
import csv
import pandas as pd
import glob
import os
from NBP_transformer import Currency_file
# from NBP_transformer import File_csv_exporter
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

df1=pd.read_csv(r'c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data/fx_nbp_merged_out/fx_nbp_merged_out.csv',sep=';',decimal='.')
df2=pd.read_csv(r'C:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/y__finance_data/dxy.csv',sep=';',decimal='.')

print(df1.head(10))
print(df2.head(10))
# Reset indeksu jeśli Date jest indeksem w df2 (np. z yfinance)
if df2.index.name == 'Date':
    df2 = df2.reset_index()

# Upewnij się, że kolumna nazywa się 'Date'
df1.rename(columns={df1.columns[0]: 'Date'}, inplace=True)
df2.rename(columns={df2.columns[0]: 'Date'}, inplace=True)

# Konwersja kolumny Date na datetime
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

merged_df=pd.merge(df1,df2,on='Date',how='inner')


folder_path=Path('c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archive_files_for_fx_data')

file_destination=folder_path/'merged_nbp_yfinance'

file_destination.mkdir(exist_ok=True)

location=file_destination/'merged_nbp_yfinance.csv'

merged_df.to_csv(location, index=False)



columns_cov = ["FX_USD/PLN", "FX_EUR/PLN", "FX_CHF/PLN","close_dxy"]

# Macierz korelacji
corr_matrix = merged_df[columns_cov].corr()
print(f'Correlation currency matrix :\n {corr_matrix}')

# Heatmapa korelacji
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation currency matrix")
plt.show()