import pandas as pd
import matplotlib.pyplot as plt
import mplcursors #helps to buid interactive charts



class Currency_file():
    def __init__(self,location,encoding,sep,index=True):
        self.location=location
        self.encoding=encoding
        self.sep=sep
        self.index=index
        self.ccy_file=pd.read_csv(self.location,encoding=self.encoding,sep=self.sep)


    def __str__(self): #will print the DataFrame 
        return str(self.ccy_file) 
    


    
    def show_columns (self):
       return self.ccy_file.columns.tolist() #returning class instance of  class Currency_file()



    def adjust_by_specific_columns(self,*args):
        """ allows to show only specifc columns , chosen by user , with specfic amount of rows"""
        draft_list=[]
        for i in args:
            draft_list.append(i)
        self.ccy_file=self.ccy_file[draft_list] # coulumns specified by input above
        self.ccy_file.reset_index(drop=True, inplace=True) #drop=True, remove old index, do not replace to column, replace the ccy_file with new data
        return self #returning class instance of  class Currency_file()
        
    def remove_rows(self,*args):
        draft_list1=[]
        for i in args:
            draft_list1.append(i)
        self.ccy_file.drop(draft_list1,inplace=True)
        self.ccy_file.reset_index(drop=True, inplace=True)
        return self #returning class instance of  class Currency_file()
    
    def rename_columns(self,**kwargs):
        # print(kwargs) # check 
        self.ccy_file.rename(columns=kwargs,inplace=True)
        return self #returning class instance of  class Currency_file()
    



    def convert_to_number(self,*args):
        for column_name in args:
            self.ccy_file[column_name]=pd.to_numeric(self.ccy_file[column_name].str.replace(',','.',regex=False), #regex=False, means that comma and dot will be treated like comma and dot. 
                                                 errors='coerce') # values not converted will stay as NaN
        return self #returning class instance of  class Currency_file()
    
 


    def convert_to_date(self,*args):
        for column_date in args:
            self.ccy_file[column_date]=pd.to_datetime(self.ccy_file[column_date])#changing the format to date
            self.ccy_file.set_index(column_date)#changing the date to index so then you can search by date and  use later in the graph as date , not as 0,1,2,3
        return self  #returning class instance of  class Currency_file()
    

class File_csv_exporter():
    def __init__(self,file,location,encoding='utf-8',sep=',',index=False):
        self.file=file
        self.location=location
        self.encoding=encoding
        self.sep=sep
        self.index=index

    def to_csv(self):
        # self.file = object from class Currency_file
        # self.file.ccy_file - Pandas DataFrame inside the object
        # to_csv(...) method responsible for creating the csv file
        self.file.ccy_file.to_csv(
            self.location,
            index=self.index,
            sep=self.sep,
            encoding=self.encoding
        )
        return self

    def __str__(self):
       # zwróci string z zawartością DataFrame
        return str(self.file.ccy_file)
    

    def show_columns(self):
        return self.file.ccy_file.columns.tolist()

        
    def mean_calc(self,*args):
        for column in args:
            result_mean=self.file.ccy_file[column].mean()
            yield (column,result_mean) #expanding yield with column result, so that later the provided parameter can be printed




    def median_calc(self,*args):
        for column in args:
            result_median=self.file.ccy_file[column].median()
            yield (column_name,result_median)




fx_usdpln_2025=Currency_file(r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/archiwum_tab_a_2025.csv","ISO-8859-2",";")

print(fx_usdpln_2025.show_columns())  # 'data', '1USD , it alows to show what columns are in the file


fx_usdpln_2025.adjust_by_specific_columns('data','1USD','1EUR').remove_rows(0)


fx_usdpln_2025.remove_rows(177,178,179).rename_columns(**{"data" : "Date"},**{"1USD":"FX_USD/PLN"},**{'1EUR':"FX_EUR/PLN"})

print(f'New colum names are: {fx_usdpln_2025.show_columns()}')

fx_usdpln_2025.convert_to_number("FX_USD/PLN","FX_EUR/PLN").convert_to_date('Date')



print(fx_usdpln_2025)


new_clean_file = File_csv_exporter(
    fx_usdpln_2025, 
    r"c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/USD_PLN_clean_current2025.csv",
    encoding="ISO-8859-2",
    sep=";"
)

# saving new csv file
new_clean_file.to_csv()

#print(f'kloumny to {new_clean_file.show_columns()}')




for column_name, mean_number in new_clean_file.mean_calc('FX_USD/PLN',"FX_EUR/PLN"): #expanding yield with column result, so that later the provided parameter can be printed

    print(f'Mean number for {column_name} is {mean_number}')



for column_name,median_number in new_clean_file.median_calc('FX_USD/PLN',"FX_EUR/PLN"):
        print(f'Mean number for {column_name} is {median_number}')


correlation=new_clean_file.file.ccy_file['FX_USD/PLN'].corr(new_clean_file.file.ccy_file["FX_EUR/PLN"])
print(f'korrelacja to : {correlation}')

# >>>>>>>>>>>>>>>>>>>>>>>





# plt.figure(figsize=(10,7)) # chart size
# plt.plot(fx_usdpln_2025.index,fx_usdpln_2025['FX_USD/PLN'],label='USD/PLN',color='blue',marker='.')
# plt.title('FX for USD/PLN rate ')
# plt.xlabel('Date')
# plt.ylabel('FX rate')
# mplcursors.cursor(hover=True)#when you hover over a point on the chart, it will show date and fx 
# plt.grid(color="gray", linestyle="--", linewidth=0.5) #turn on the grid

# plt.show()
                      