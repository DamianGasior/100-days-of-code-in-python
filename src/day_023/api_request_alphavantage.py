import requests
import time
import pandas as pd
from datetime import date
from pathlib import Path
import requests_cache
import logging

# requests_cache.clear()
import sqlite3
import pickle
import os
from dotenv import load_dotenv  # module which allows to read .env file

#Frist file for getting the data

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")  # loads are variables from .env file and caches those
API_KEY = os.getenv(
    "apikey_alpha_vantage"
)  # use the variable loaded from the line above


class Underlying_request_details:
    cache_path = BASE_DIR / "alpha_cache"
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    def __init__(self, symbol, function, outputsize, datatype, apikey=API_KEY):
        self.apikey = apikey
        self.symbol = symbol
        self.function = function
        self.outputsize = outputsize
        self.datatype = datatype
        self.cache_path = (
            Path(self.__class__.cache_path) / f"{symbol}"
        )  # using  class atrribute
        self.db_file = Path(self.cache_path).with_suffix(".sqlite")

    def cache_manager(self):

        requests_cache.install_cache(
            self.cache_path,
            backend="sqlite",
            expire_after=100000,
            allowable_methods=("GET", "POST"),
            serializer="pickle",
        )

    def to_dict_params(self):
        return self.__dict__

    def request_to_ext_api(self):
        self.cache_manager()
        params = self.to_dict_params()
        url = "https://www.alphavantage.co/query"
        try:
            resp = requests.get(url, params=params)
            resp.raise_for_status()
            logging.info(f"Response type is : {resp}")

        except requests.exceptions.Timeout:
            print("Error: Server did not respond.Try again later.")
            return None

        except requests.exceptions.HTTPError as e:
            print(f"Http error: {e}")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Another error type: {e}")
            return None

        if resp.status_code == 200 and "Information" in resp.json():
            timeout_message = resp.json()
            print(
                f"Limit API was reached, see comment : {timeout_message},wait 60 seconds please"
            )
            time.sleep(60)
            return self.request_to_ext_api()
        elif resp.status_code == 200 and (getattr(resp, "from_cache", False)) is False:
            logging.info("response was succesfull (200)")
        elif getattr(resp, "from_cache", False) is True:
            logging.info("Response is from cache.")
        else:
            print(f"Response failed : {resp.status_code}")



        response = resp.json()

        # print(json.dumps(response,indent=4)) # to see what is the json format response
        return response

    def read_all_keys_values_from_api(self):
        # reads all the keys and values from request_to_ext_api() , from api or caches
        resp = self.request_to_ext_api()
        # resp=resp.json()
        for key, value in resp.items():
            print(f'KEY IS : {key}, ":", VALUE IS : {value} \n')

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
        print("URL:", resp_cached2["url"])

        # Dane JSON odpowiedzi

        conn.close()

# #Second File for DataFrame

# class Underlying_data_frame:
#     def __init__(self, response_from_alpha, underlying_request:Underlying_request_details):
#         self.stock_symbol=underlying_request.symbol #class instance from Underlying_request_details
#         self.response_from_alpha = response_from_alpha

#         # print( self.response_from_alpha)
#     #    stock_symbol=self.response_from_alpha.symbol
#         # print(stock_symbol)

#     def __getattr__(self,name): # dunder method, it allows to treat the class instance as dataframe
#         return getattr(self.response_from_alpha,name)

#     def transform(self, key_paremeter, orient="index"):
#         '''based on the key_parameter we take from a set of dictionaries , the proper key = key_parameters;
#         After the key is identified the Value is another set of dictionaries: 
#     The structure of self.response_from_alpha is as follows:
#     {
#         'Time Series (Daily)': {
#             '2025-10-10': {
#                 '1. open': '254.9400',
#                 '2. high': '256.3800',
#                 '3. low': '244.0000',
#                 '4. close': '245.2700',
#                 '5. volume': '61999098'
#             },
#             '2025-10-09': {
#                 '1. open': '257.8050',
#                 '2. high': '258.0000',
#                 '3. low': '253.1400',
#                 '4. close': '254.0400',
#                 '5. volume': '38322012'
#             },
#             ...
#         }...;
#               Since 'orient' is set to 'index', the outer dictionary keys (dates) become DataFrame rows (index).'''
#         self.response_from_alpha = pd.DataFrame.from_dict(
#             self.response_from_alpha[key_paremeter], orient
#         )
#         return self
    
#     def set_date_as_index(self):
#         self.response_from_alpha.index.name = (
#             "Date"  # assiging the name of the columns as 'Date' which is our index
#         )
#         self.response_from_alpha.index = pd.to_datetime(self.response_from_alpha.index).date # .date function  is enough, no need for dt.date, as .date is typical for index
#         # self.response_from_alpha.index=self.response_from_alpha.index.dt.date
#         #changing the columns ( apart of date one ) to int or float 
#         for col in self.response_from_alpha:
#             if not pd.api.types.is_datetime64_any_dtype(self.response_from_alpha[col]): # function is checking if each colums is not in a datetime format
#                 self.response_from_alpha[col]=pd.to_numeric(self.response_from_alpha[col],errors='coerce') # applying the change, if not a number , then populate NaN
#         return self

#     def __str__(self):
#         return str(self.response_from_alpha.head(15))

#     def show_columns(self):
#         print(f'type to: {type(self.response_from_alpha)}')
#         print(self.response_from_alpha.dtypes)
#         print(self.response_from_alpha.head())
#         return self.response_from_alpha.columns.tolist()

#     def column_rename(self, **kwargs):
#         # columns #thnink if it should be alist or a dict or waht ?
#         self.response_from_alpha.rename(columns=kwargs, inplace=True)
#         return self
    

# Third file for metrics,
#pass here the data frame  - set is as class, which  has already an index , in the  class attribute , contain symbol , start and end date. 


    # def price_chng_perct(self):
    #     self.response_from_alpha['return']=(self.response_from_alpha['close'].pct_change()*100).round(4)
        
    #     return self.response_from_alpha
    
    # def worst_and_best(self):
        
    #     # row with the worst ( min) and the best (max)  performance, change percantage on the day
    #     worst_idx = self.response_from_alpha['return'].idxmin()
    #     best_idx  = self.response_from_alpha['return'].idxmax()


    #     # values for the row above with the actual numbers from column 'return', with the help of .loc ( locator?)I can get with the help of label for column and row
    #     worst_val = self.response_from_alpha.loc[worst_idx, 'return']
    #     best_val  = self.response_from_alpha.loc[best_idx, 'return']

    #     #the same as worst_idx and   best_idx , just assiging to variable with date
    #     worst_date = worst_idx
    #     best_date = best_idx
    
    #    # price level for that specifc day, the best and the worst day
    #     close_price_on_worst = self.response_from_alpha.loc[worst_idx, 'close']
    #     close_price_on_best = self.response_from_alpha.loc[best_idx, 'close']

    #     stocks=self.stock_symbol

 
    #     result_df=pd.DataFrame({
    #         'Date': [worst_date,best_date],
    #         'Symbol':[stocks,stocks],
    #         'close ':[ close_price_on_worst, close_price_on_best],
    #         "Type": ["Worst", "Best"],
    #         "Return": [ worst_val, best_val]
    #     })
        
    #     print( result_df)
    

    # def std_dev(self):
    #     print('standard deviation')

    #     stand_dev=self.response_from_alpha['close'].std()
    #     start_date=self.response_from_alpha.index.min()
    #     end_date=self.response_from_alpha.index.max()
    #     print(f"Standard deviation for {self.stock_symbol} is {stand_dev}")
    #     result_st_dev=pd.DataFrame({
    #         'Symbol':[self.stock_symbol],
    #         'Start_date':[start_date],
    #         'End_date':[end_date],
    #         'Std_dev':[stand_dev]
    #     })
    #     print(result_st_dev)

    # #add average price, high and low for a sepcifc period, and the price for start date and end date. 



        


 


# def main():
#     apple_stock = Underlying_request_details(
#         "AAPL", "TIME_SERIES_DAILY", "compact", "json"
#     )

#     test = apple_stock.request_to_ext_api()
#     print(test)

#     # print(apple_stock.read_all_keys_values_from_api())
#     apple_stock_df = Underlying_data_frame(test,apple_stock)
#     apple_stock_df = apple_stock_df.transform("Time Series (Daily)")
#     apple_stock_df = apple_stock_df.set_date_as_index()
   

#     apple_stock_df.column_rename(
#         **{"1. open": "open"},
#         **{"2. high": "high"},
#         **{"3. low": "low"},
#         **{"4. close": "close"},
#         **{"5. volume": "volume"},
#     )
#     apple_stock_df.price_chng_perct()
#     # print(apple_stock_df.show_columns())
#     print(apple_stock_df.worst_and_best())
#     print(apple_stock_df.std_dev())


# # napisac funkcje ktra pokaze  ajgorszy i najlepszyt dzien i wtdy mozna tez ladnie uderzyc o news na ten dzien


# # moze dan z stad wyciagnac pozniej, by sammeu nie  liczcy ? choc juz to mam policzone  w incyh plikach. 

# if __name__ == "__main__":
#     main()

    # def __init__(self,symbol, function, outputsize,datatype,apikey='POS5M1VCF1GC1VM3'):




# apple_stock_df.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
# print(apple_stock_df.show_columns())
# print(apple_stock_df)

# apple_stock.read_caches()


# xom_stock=Underlying_request_details('XOM',"TIME_SERIES_DAILY","compact" ,"json")

# xom_test=xom_stock.request_to_ext_api()
# # print(test)
# # Underlying_request_details.check_for_caches()


# xom_stock.read_all_keys_values_from_api()

# # xom_stock_df=Underlying_data_frame(xom_test,"Time Series (Daily)")
# # print(xom_stock_df)

# # print(xom_stock_df.show_columns())


# # xom_stock_df.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
# # print(xom_stock_df.show_columns())
# # print(xom_stock_df)

# # print('CACHEEEEEEEEEEEEES')
