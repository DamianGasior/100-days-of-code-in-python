import requests
import time
import pandas as pd
from datetime import date
from pathlib import Path
import requests_cache
import logging
import sqlite3
import pickle
import os
from dotenv import load_dotenv  # module which allows to read .env file

from api_request_alphavantage import Underlying_request_details
from stock_data_frame import Underlying_data_frame


class Underlying_metrics:
    def __init__(self,underlying_request:Underlying_request_details,underlying_df:Underlying_data_frame):
         self.stock_symbol=underlying_request.symbol
         self.underlying_df=underlying_df
    


    def price_chng_perct(self):
        self.underlying_df['return']=(self.underlying_df['close'].pct_change()*100).round(4)
        
        return self.underlying_df

    def worst_and_best(self):
        
        # row with the worst ( min) and the best (max)  performance, change percantage on the day
        worst_idx = self.response_from_alpha['return'].idxmin()
        best_idx  = self.response_from_alpha['return'].idxmax()


        # values for the row above with the actual numbers from column 'return', with the help of .loc ( locator?)I can get with the help of label for column and row
        worst_val = self.response_from_alpha.loc[worst_idx, 'return']
        best_val  = self.response_from_alpha.loc[best_idx, 'return']

        #the same as worst_idx and   best_idx , just assiging to variable with date
        worst_date = worst_idx
        best_date = best_idx
    
       # price level for that specifc day, the best and the worst day
        close_price_on_worst = self.response_from_alpha.loc[worst_idx, 'close']
        close_price_on_best = self.response_from_alpha.loc[best_idx, 'close']

        stocks=self.stock_symbol

 
        result_df=pd.DataFrame({
            'Date': [worst_date,best_date],
            'Symbol':[stocks,stocks],
            'close ':[ close_price_on_worst, close_price_on_best],
            "Type": ["Worst", "Best"],
            "Return": [ worst_val, best_val]
        })
        
        print( result_df)
    

    def std_dev(self):
        print('standard deviation')

        stand_dev=self.response_from_alpha['close'].std()
        start_date=self.response_from_alpha.index.min()
        end_date=self.response_from_alpha.index.max()
        print(f"Standard deviation for {self.stock_symbol} is {stand_dev}")
        result_st_dev=pd.DataFrame({
            'Symbol':[self.stock_symbol],
            'Start_date':[start_date],
            'End_date':[end_date],
            'Std_dev':[stand_dev]
        })
        print(result_st_dev)

    #add average price, high and low for a sepcifc period, and the price for start date and end date. 
    
