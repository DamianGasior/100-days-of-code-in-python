import requests
import pandas as pd
from datetime import date
from pathlib import Path
import json
import requests_cache
# requests_cache.clear() 
import sqlite3
import pickle




class Underlying_request_details():
    
    BASE_DIR=Path(__file__).parent
    # cache_path =BASE_DIR/'alpha_cache'/'alpha_cache'
    cache_path =BASE_DIR/'alpha_cache'
    cache_path .parent.mkdir(parents=True, exist_ok=True)

 


    def __init__(self,symbol, function, outputsize,datatype,apikey='POS5M1VCF1GC1VM3'):
        self.apikey=apikey
        self.symbol=symbol
        self.function = function
        self.outputsize=outputsize  
        self.datatype=datatype
        # self.cache_path=self.__class__.cache_path # using  class atrribute 
        self.cache_path=Path(self.__class__.cache_path)/f'{symbol}' # using  class atrribute 
        self.db_file=Path(self.cache_path).with_suffix('.sqlite')





    def cache_manager(self):
        
        requests_cache.install_cache(self.cache_path, backend='sqlite', expire_after=10000, allowable_methods=('GET', 'POST'), serializer='pickle')
        
      
    def to_dict_params(self):
        return self.__dict__

    def request_to_ext_api(self):
        self.cache_manager()
        params=self.to_dict_params()
        url='https://www.alphavantage.co/query'
        resp = requests.get(url, params=params)
        print(resp.url)
        if resp.status_code==200 and (getattr(resp,'from_cache',False)) is False :                                 
            print("response was succesfull (200)")
        elif getattr(resp,'from_cache',False) is True:
            print('Reqsponse is from cache. ')
        else:
            print(f"Response failed : {resp.status_code}")
        response=resp.json()
        # print(json.dumps(response,indent=4)) # to see what is the json format response 
        return response
    
    def read_all_keys_values_from_api(self):
        # reads all the keys and values from request_to_ext_api() , from api or caches
        resp=self.request_to_ext_api()
        # resp=resp.json()
        for key, value in resp.items():
            print(f'{key}, ":", {value} \n' )
    
    
    def check_for_caches(self):
        # połączenie z bazą
        conn = sqlite3.connect(self.db_file)
        # lista tabel
        tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
        print("Tabele w cache DB:\n", tables)
        if "responses" in tables["name"].values:
            df = pd.read_sql("SELECT * FROM responses", conn)
            print("Responses rows:", len(df))
        else:
            print("Brak tabeli responses (jeszcze nic nie zostało zapisane).")
        conn.close()
    

    def read_caches(self):
        print(self.db_file)
        conn = sqlite3.connect(self.db_file)
        df = pd.read_sql("SELECT * FROM responses", conn)
        print(df.columns.tolist())
        # Rozpakowujemy pierwszy rekord\
   
        raw_value2 = df.loc[0, "value"]
        resp_cached2 = pickle.loads(raw_value2)
        print(resp_cached2)
       

        # URL requesta
        print("URL:", resp_cached2['url'])

        # Dane JSON odpowiedzi

        conn.close()




class Underlying_data_frame():
    def __init__(self,response_from_alpha,key_paremeter):
        self.response_from_alpha=response_from_alpha
        self.transform(key_paremeter)

        

    def transform(self,key_paremeter,orient='index'):
        self.response_from_alpha=pd.DataFrame.from_dict(self.response_from_alpha[key_paremeter],orient)
        self.response_from_alpha.index.name='Date' # assiging the name of the columns as 'Date' which is our index
        self.response_from_alpha.index=pd.to_datetime(self.response_from_alpha.index)
        return  self.response_from_alpha
 
    def __str__(self):
        return str(self.response_from_alpha.head(15))


    def show_columns(self):
        return self.response_from_alpha.columns.tolist()

    def column_rename(self,**kwargs):
        # columns #thnink if it should be alist or a dict or waht ? 
        self.response_from_alpha.rename(columns=kwargs,inplace=True)
        return self.response_from_alpha

    # def method_for index and transforming for date_time






    # def __init__(self,symbol, function, outputsize,datatype,apikey='POS5M1VCF1GC1VM3'):


apple_stock=Underlying_request_details('AAPL',"TIME_SERIES_DAILY","compact" ,"json")

test=apple_stock.request_to_ext_api()
# print(test)
# Underlying_request_details.check_for_caches()
# apple_stock.read_caches()

apple_stock.read_all_keys_values_from_api()

apple_stock_df=Underlying_data_frame(test,"Time Series (Daily)")
print(apple_stock_df)

print(apple_stock_df.show_columns())


apple_stock_df.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
print(apple_stock_df.show_columns())
print(apple_stock_df)

# apple_stock_df



apple_stock=Underlying_request_details('AAPL',"TIME_SERIES_DAILY","compact" ,"json")

test=apple_stock.request_to_ext_api()
# print(test)
# Underlying_request_details.check_for_caches()
# Underlying_request_details.read_caches()

apple_stock.read_all_keys_values_from_api()

apple_stock_df=Underlying_data_frame(test,"Time Series (Daily)")
print(apple_stock_df)

print(apple_stock_df.show_columns())


apple_stock_df.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
print(apple_stock_df.show_columns())
print(apple_stock_df)

apple_stock.read_caches()


xom_stock=Underlying_request_details('XOM',"TIME_SERIES_DAILY","compact" ,"json")

xom_test=xom_stock.request_to_ext_api()
# print(test)
# Underlying_request_details.check_for_caches()


xom_stock.read_all_keys_values_from_api()

# xom_stock_df=Underlying_data_frame(xom_test,"Time Series (Daily)")
# print(xom_stock_df)

# print(xom_stock_df.show_columns())


# xom_stock_df.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
# print(xom_stock_df.show_columns())
# print(xom_stock_df)

# print('CACHEEEEEEEEEEEEES')



