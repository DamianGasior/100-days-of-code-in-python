import yfinance as yf
import csv
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path # class  Path from mudle patlib jas ready methoed which help to manage paths  in a more convenient way

folder=Path("c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/y__finance_data")

draft_list={}
count=0
for files in folder.iterdir(): # it will iterate over files and folders
    if files.is_file() and files.suffix=='.csv': # checks if the file exists and if the file has a csv extension < from Pathlib library 
        count+=1
        symbol=f'df{count}'
        draft_list[symbol]=(f'{files.as_posix()}')  #as_posix() will alwyas give '/' independently form the system


print(draft_list)


    


class Yahoo_file():
    def __init__(self,location,encoding="ISO-8859-2",sep=';' , decimal='.',index=True):
        self.location=location
        self.encoding=encoding
        self.sep=sep
        self.decimal=decimal
        self.index=index
        self.y_file=pd.read_csv(self.location,encoding=self.encoding,sep=self.sep)


    def __str__(self): #will print the DataFrame 
        return str(self.y_file.head(8))
    
    def _getitem_(self,key):
        return self.y_file[key]
    
draft_list2={}

for key,value in draft_list.items():
    obj_class=Yahoo_file(value)
    draft_list2[key]=obj_class.y_file #storing data frame to dictionary
        
        
for df in  draft_list2:
    print (draft_list2[df].head(10))



for df in draft_list2.values():
    df.rename(columns={df.columns[0]: 'Date'}, inplace=True) #cehcking if the first column is called 'Date'
    if  df.index.name == 'Date':
        df = df.reset_index() #applying reset index, so that Date is set to normal column, and an numerical index is applied
    df['Date'] = pd.to_datetime(df['Date']) #converting the column 'Date' to be in formate datetime64
    # print('operacja zrobiona')


merged_df=(
    pd.concat(
        [df.set_index("Date") for df in draft_list2.values()], #'Date' is changed to index, pd.conc, will merge based on common 'Date;
        axis=1, #merging the files based on columns, expanding to the right, more columns, : axis=0 , means, you are adding more rows
        join="inner") #inner means we merge only by those dates which are common accross all df's, it can be 'outer' as well, we concac, there where is no match, yo put - Nan
        # .reset_index()#'Date' passed as simple column
    )


folder_path=Path('c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022')

file_destination=folder_path /'y_finance_merged_all_files'

file_destination.mkdir(exist_ok=True)

location=file_destination/'y_finance_merged_all_files.csv'

merged_df.to_csv(location, index=True)  


df_merged=pd.read_csv(location, sep=";", decimal=".", encoding="utf-8")

print(df_merged.head(10))

print(type(df_merged))

print(df_merged.columns.tolist())

columns_cov = ["close_dxy", "close_usd_pln", "close_eur_pln","close_wig","close_sp_500","close_dax","close_stoxx50e"]

# Macierz korelacji

corr_matrix = merged_df[columns_cov].corr()
print(f'Correlation matrix : \n{corr_matrix}')

# Heatmapa korelacji
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation matrix")
plt.show()


merged_df['corr_usdpln_dxy_30d']=merged_df["close_dxy"].rolling(window=30).corr(merged_df['close_usd_pln'])


merged_df['corr_wig_sp500_30d']=merged_df["close_wig"].rolling(window=30).corr(merged_df['close_sp_500'])

merged_df['returns_wig']=merged_df["close_wig"].pct_change()


merged_df['returns_sp_500']=merged_df["close_sp_500"].pct_change()

# print(merged_df[["Date","close_dxy", "close_usd_pln",'corr_usdpln_dxy_30d', "close_wig",'returns_wig',"close_sp_500",'returns_sp_500','corr_wig_sp500_30d']].tail(40))


# print(f'Macierz korelacji ddddd : \n{rolling_corr_30d}')

# plt.figure(figsize=(8,6))
# sns.heatmap(merged_df["rolling_corr_30d"], annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
# plt.title("Macierz :")
# plt.show()


#beta wobec wszystkich 

benchmark = 'close_sp_500'

returns=merged_df[["close_dxy", "close_usd_pln", "close_eur_pln","close_wig","close_dax","close_stoxx50e",benchmark]].pct_change().dropna()

betas=returns.drop(columns=[benchmark]).apply(lambda x: x.cov(returns[benchmark])/returns[benchmark].var())


print(f'beta against {benchmark}  : \n {betas}')



benchmark1 = 'close_dax'

returns1=merged_df[["close_usd_pln","close_wig","close_stoxx50e",benchmark1]].pct_change().dropna()

betas1=returns1.drop(columns=[benchmark1]).apply(lambda x: x.cov(returns1[benchmark1])/returns1[benchmark1].var())

print(f'\nbeta against {benchmark1}  : \n {betas1}')


