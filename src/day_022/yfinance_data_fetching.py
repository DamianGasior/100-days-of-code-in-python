import yfinance as yf
import csv
import pandas as pd
import glob
import os
from NBP_transformer import Currency_file
# from NBP_transformer import File_csv_exporter
import seaborn as sns
import matplotlib.pyplot as plt




class Yahoo_data():
    def __init__(self,folder_path,raw_file_name,output_file_name,sep=';',encoding='utf-8',index=True): #raw_file_name='y_data',
        self.folder_path=folder_path
        self.file_destination=self._destination(folder_path,raw_file_name)
        self.file_location=self._location(self.file_destination,output_file_name)
        self.sep=sep
        self.encoding=encoding
        self.index=index
        if os.path.exists(self.file_location):
            self.yahoo_file=pd.read_csv(self.file_location)
        else:
            self.yahoo_file=None
          

    @staticmethod
    def _destination(folder_path,raw_file_name):
        file_destination=os.path.join(folder_path,raw_file_name)#'y_data' , name of the folder , where the file will be placed
        os.makedirs(file_destination,exist_ok=True) # if the folder, does exist, do not throw an error, continue to process/ 
        # location=os.path.join(file_destination,output_file_name) #'dxy.csv' , title of the file, which will be saved as processing result
        return file_destination
    
    @staticmethod
    def _location(file_destination,output_file_name):
        location=os.path.join(file_destination,output_file_name) #'dxy.csv'
        return location



    def yf_download(self,data_name,start_date,end_date):
        self.yahoo_file=yf.download(data_name,start_date,end_date)
        return self.yahoo_file
        

    def set_columns(self,column_names):
        self.yahoo_file.columns=column_names
        return self.yahoo_file
        

    def file_convert_csv(self):
        self.yahoo_file.to_csv(self.file_location,
                    index=self.index,
                    sep=self.sep,
                    encoding=self.encoding)
        return self.yahoo_file
    
    def remove_columns(self,*args):
        for i in args:
            self.yahoo_file.drop(i,axis=1,inplace=True) # coulumns specified by input above
        return self.yahoo_file #returning class instance of  


    def show_columns (self):
        return self.yahoo_file.columns.tolist() #returning class instance of  class Currency_file()

    def show_head (self,param):
        return self.yahoo_file.head(param) #returning class instance of  class Currency_file()


def main():

    common={'folder_path':r'c:/Users/Admin/Desktop/Python/repository_dg/100-days-of-code-in-python/src/day_022/',
        'raw_file_name' :'y__finance_data',
            'set_columns': ['close_dxy','High','Low','Open','Volume'], #<<<<< this needs to be adjusted and moved from common to a differnet one , or take the 'close'_key
            'remove_columns':['High','Low','Open','Volume'],
            'start':"2018-01-01",
            'end':'2025-09-12'}
    
    list_of_underlyings=['dxy','usd_pln','eur_pln','sp_500','dax','stoxx50e']
    underlyings={'dxy':'DX-Y.NYB',
                 'usd_pln':'USDPLN=X',
                 'eur_pln':'EURPLN=X',
                 'sp_500':"^GSPC",
                 'dax':'^GDAXI',
                 'stoxx50e':'^STOXX50E'
                 }
    print(type(list_of_underlyings))
    print(type(underlyings))


    for stock in list_of_underlyings:
        symbol=underlyings[stock]
        # print(f'symbol to {symbol}')
        underlying=Yahoo_data(folder_path=common['folder_path'],
                    raw_file_name=common['raw_file_name'],             #'y_data',
                    output_file_name= f'{stock}.csv')
               
        underlying.yf_download(symbol, common['start'], common['end'])
        underlying.set_columns([f'close_{stock}','High','Low','Open','Volume'] )
        underlying.remove_columns(common['remove_columns'])
        # underlying.rename(columns=[f'close_{underlying}'])
        # print(dxy.show_head(8))
        underlying.file_convert_csv()
        print(underlying.show_head(8))






    # Wig data were downloaded manually from stooq.pl page, could not find it in yahoo


if __name__=="__main__":
    main()

   



