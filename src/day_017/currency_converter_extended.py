# Task: Advanced Currency Converter
# Requirements:
# Create a class CurrencyConverter, which:
# - has a dictionary rates storing exchange rates in relation to PLN 
#   (e.g., {"USDPLN": 4.2, "EURPLN": 4.5}).
#
# - allows conversion in both directions:
#   PLN ➝ foreign currency
#   foreign currency ➝ PLN
#
# Add methods:
# - convert_to_foreign(self, amount_pln) – converts PLN → FX
# - convert_to_pln(self, amount_fx) – converts FX → PLN
#
# Add a class method:
# - update_rate(cls, currency, rate) – updates or adds a new currency and its rate.
#
# Add validation:
# - if the currency is not in the dictionary, raise an exception (ValueError).
#
# Add a helper method:
# - list_rates(cls) – prints available currencies and their rates.

import logging

logging.basicConfig(level=logging.WARNING)

class CurrencyConverter:
    rates={'USDPLN' : 4.2 , 'EURPLN' : 4.0 , 'JPYPLN' : 0.1 , 'SEKPLN' : 2.34}


    def __init__(self,fx_pair): #argumenty
        self.fx_pair=self.fx_pair_check(fx_pair)
        self.rate=self.rates.get(self.fx_pair)

    
    def convert_to_foreign_ccy(self,amount):
        ''''transform the amount from PLN to foreign currency'''
        if self.fx_pair in self.rates:
            self.rate=self.rates.get(self.fx_pair)
            foreign_amount=amount/self.rate
            return  f'Cash in foreign currency is : {foreign_amount} '
        else:
            raise ValueError(f'{self.fx_pair} not  in {self.rates}')

        
    def convert_to_pln(self,amount_fx):
        ''''transform the amount from  foreign currency to PLN'''
        self.fx_pair=self.search_fx_pair(self.rates,self.fx_pair)
        if self.fx_pair != None:
            logging.debug ('fx pair to %d',self.fx_pair)
            self.rate=self.rates.get(self.fx_pair)
            logging.debug (self.rate)
            amount_to_pln=amount_fx/(1/self.rate)
            return f'Cash in PLN is: {amount_to_pln}'
        else:
            raise ValueError(f'{self.fx_pair} not  in {self.rates}')


    @staticmethod
    def search_fx_pair(rates,fx_pair):
        for i in rates.keys():
            if fx_pair in i:
                return i
        return None


    @classmethod
    def update_rates(cls,fx_pair,rate):
        '''update the library with new entries''' 
        rate=cls.rate_check(rate)
        fx_pair=cls.fx_pair_check(fx_pair)
        cls.rates[fx_pair]=rate
        logging.debug ('Dict  "rates" was udpated with new entries')
        logging.debug (cls.rates)





    @staticmethod
    def rate_check(rate):
        rate =float(rate)
        return rate
        
    @staticmethod
    def fx_pair_check(fx_pair):
        fx_pair =str(fx_pair)
        return fx_pair


    @staticmethod
    def format_amount(amount_pln):
        if isinstance(amount_pln,float):
            amount_pln=str(amount_pln)
            return amount_pln + ' PLN'
        else:
            amount_pln=float(amount_pln)
            amount_pln=str(amount_pln)
            return amount_pln + ' PLN'
        
    @classmethod
    def list_rates(cls):
        print('Available FX pairs are: ')
        for key,values in cls.rates.items():
            print(f'{key} - {values}')
        



c0=CurrencyConverter('EURPLN')
print(c0.convert_to_foreign_ccy(200))


c2=CurrencyConverter('EUR')
print(c2.convert_to_pln(25))

available_ccy_pairs=CurrencyConverter.list_rates()

