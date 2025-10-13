import pandas as pd
from datetime import date
from pathlib import Path

from dotenv import load_dotenv  # module which allows to read .env file

from api_request_alphavantage import Underlying_request_details



class Underlying_data_frame:
    def __init__(self, response_from_alpha, underlying_request:Underlying_request_details):
        self.stock_symbol=underlying_request.symbol #class instance from Underlying_request_details
        self.response_from_alpha = response_from_alpha
        

        

        # print( self.response_from_alpha)
    #    stock_symbol=self.response_from_alpha.symbol
        # print(stock_symbol)

    def __getattr__(self,name): # dunder method, it allows to treat the class instance as dataframe
        return getattr(self.response_from_alpha,name)

    def transform(self, key_paremeter, orient="index"):
        '''based on the key_parameter we take from a set of dictionaries , the proper key = key_parameters;
        After the key is identified the Value is another set of dictionaries: 
    The structure of self.response_from_alpha is as follows:
    {
        'Time Series (Daily)': {
            '2025-10-10': {
                '1. open': '254.9400',
                '2. high': '256.3800',
                '3. low': '244.0000',
                '4. close': '245.2700',
                '5. volume': '61999098'
            },
            '2025-10-09': {
                '1. open': '257.8050',
                '2. high': '258.0000',
                '3. low': '253.1400',
                '4. close': '254.0400',
                '5. volume': '38322012'
            },
            ...
        }...;
              Since 'orient' is set to 'index', the outer dictionary keys (dates) become DataFrame rows (index).'''
        self.response_from_alpha = pd.DataFrame.from_dict(
            self.response_from_alpha[key_paremeter], orient
        )
        return self
    
    def set_date_as_index(self):
        self.response_from_alpha.index.name = (
            "Date"  # assiging the name of the columns as 'Date' which is our index
        )
        self.response_from_alpha.index = pd.to_datetime(self.response_from_alpha.index).date # .date function  is enough, no need for dt.date, as .date is typical for index
        # self.response_from_alpha.index=self.response_from_alpha.index.dt.date
        #changing the columns ( apart of date one ) to int or float 
        for col in self.response_from_alpha:
            if not pd.api.types.is_datetime64_any_dtype(self.response_from_alpha[col]): # function is checking if each colums is not in a datetime format
                self.response_from_alpha[col]=pd.to_numeric(self.response_from_alpha[col],errors='coerce') # applying the change, if not a number , then populate NaN
        return self

    def __str__(self):
        return str(self.response_from_alpha.head(15))

    def show_columns(self):
        print(f'type to: {type(self.response_from_alpha)}')
        print(self.response_from_alpha.dtypes)
        print(self.response_from_alpha.head())
        return self.response_from_alpha.columns.tolist()

    def column_rename(self, **kwargs):
        # columns #thnink if it should be alist or a dict or waht ?
        self.response_from_alpha.rename(columns=kwargs, inplace=True)
        return self
    

# Third new class will be ther ->class Underlying_metrics:

    def price_chng_perct(self):
        self.response_from_alpha['return']=(self.response_from_alpha['close'].pct_change()*100).round(4)
        
        return self.response_from_alpha

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
    
