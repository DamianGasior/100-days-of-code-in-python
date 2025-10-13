from api_request_alphavantage import Underlying_request_details,Underlying_data_frame


class UnderlyingBuilder:
    def __init__(self,underlying_reuqestor:Underlying_request_details):
        self.underlying_reuqestor=underlying_reuqestor

        if  self.underlying_reuqestor.function=="TIME_SERIES_DAILY":
            self.key_paremeter="Time Series (Daily)"
        
        # print(f'symbol to {self.underlying_reuqestor.symbol}')
        

    

    def run_pipeline(self,underlying_reuqestor) :
        stock=self.underlying_reuqestor.request_to_ext_api()
        data_frame_builder =Underlying_data_frame(stock,underlying_reuqestor)
        data_frame_builder.transform(self.key_paremeter)
        data_frame_builder.set_date_as_index()
        data_frame_builder.column_rename(**{'1. open': 'open'},**{'2. high': 'high'},**{'3. low': 'low'},**{'4. close': 'close'},**{'5. volume': 'volume'})
        
        # data_frame_builder.show_columns()
        # stock=self.underlying_reuqestor.read_caches()
        print(data_frame_builder)
        print(data_frame_builder.show_columns())
        # print(data_frame_builder.filter(items=['Date','close']))
        print(data_frame_builder.price_chng_perct())
        # print(data_frame_builder.show_columns())


        result_worst_and_best=data_frame_builder.worst_and_best()
        print(result_worst_and_best)

        stand_deviation_metrics=data_frame_builder.std_dev()
        print(stand_deviation_metrics)
        # print(data_frame_builder.show_columns())



def main():
    
    #config 
    function="TIME_SERIES_DAILY"
    outputsize="compact"
    datatype="json"
    symbol='MSFT'
    # return_column_name='close'


    underlying_reuqestor=Underlying_request_details(symbol=symbol,function=function,outputsize=outputsize,datatype=datatype)
    pipeline=UnderlyingBuilder(underlying_reuqestor).run_pipeline(underlying_reuqestor)
    
      

if __name__=="__main__":
    main()