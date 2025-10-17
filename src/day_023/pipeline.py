from api_request_alphavantage import Underlying_request_details
from stock_data_frame import Underlying_data_frame
from metrics_calcs import Underlying_metrics
from collections import deque


class UnderlyingBuilder:
    def __init__(self,underlying_reuqestor:Underlying_request_details):
        self.underlying_reuqestor=underlying_reuqestor

        

        if  self.underlying_reuqestor.function=="TIME_SERIES_DAILY":
            self.key_paremeter="Time Series (Daily)"
        
      
        

    

    def run_pipeline(self,underlying_reuqestor) :
        stock=self.underlying_reuqestor.request_to_ext_api()
        print(type(stock))
        data_frame_builder =Underlying_data_frame(stock,self.key_paremeter,underlying_reuqestor)
        print('Type dla "data_frame_builder" to : ',type(data_frame_builder))
        print(data_frame_builder)
       
        
     
        data_frame_builder_with_calcs=Underlying_metrics(self.underlying_reuqestor,data_frame_builder) #this was key , passing here the class parameters , and dataframe
        # print(type(data_frame_builder_with_calcs))

        print(data_frame_builder_with_calcs.price_chng_perct())
        print(data_frame_builder_with_calcs.head())
        
        print(type(data_frame_builder))
        print(type(data_frame_builder_with_calcs))


        result_worst_and_best=data_frame_builder_with_calcs.worst_and_best()
        print(result_worst_and_best)

        stand_deviation_metrics=data_frame_builder_with_calcs.std_dev()
        print(stand_deviation_metrics)




def main():
    
    queue_of_requests=deque()

    symbol_list=['SPY','MSFT']
  

    while symbol_list:
        for code in symbol_list:
            if len(symbol_list) >= 1:
                underlying_reuqestor=Underlying_request_details(
                symbol= symbol_list.pop(0),
                function="TIME_SERIES_DAILY",
                outputsize="compact",
                datatype="json")
            else:
                raise ValueError('Missing Underlyin code')

        queue_of_requests.append(underlying_reuqestor)
        print(len(queue_of_requests))
    

    while queue_of_requests:

        underlying_reuqestor=queue_of_requests.popleft()

        pipeline=UnderlyingBuilder(underlying_reuqestor).run_pipeline(underlying_reuqestor)

    

if __name__=="__main__":
    main()