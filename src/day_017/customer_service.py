# # Imagine you need to create a simple queue system to manage clients at the bank

# # Requirements:
# 1.Create a customer class , which has : 
# - name – clients name
# - priority – priorytet (np. 1 = VIP, 2 = normal client).

# 2. Add method __str__, which returns clients description:
# - "[1] Jan Kowalski" or  "[2] Adam Nowak".

# 3. Create a class  BankQueue, which :
# - has an internal list of clients queue,
# - method  add_customer(customer) – adds the client to the queue
# - method/s which will  return and delete the first  Vip client from the queue, if there is any; otherwise the first normal one 
# # method  show_queue() – displays the actual queue in a user friendly format

# # Edge case, in case the queue is empty (np. raise ValueError with  "There were no clients at all in the queue").

class Customer:
    def __init__(self,name,priority=None):
        self.name=name
        self.priority=priority

    def __str__(self):
        return f'Priority: {self.priority} and the client is: {self.name}'

class BankQueue:
    client_queue=[]
    
    @classmethod
    def add_customer(cls,customer):
        cls.client_queue.append(customer)
        print(cls.client_queue)
        


    @classmethod
    def show_queue(cls):
        if not cls.client_queue:  #simple check which allows , to verfiy if list is empty
            raise IndexError ('There are no client in queue')
            
        else:
            for customer in cls.client_queue:
                print(customer)  #



# method which  looks for the first vip client
    @classmethod
    def search_vip(cls):
        for iks,customer in enumerate(cls.client_queue):
            if customer.priority ==1:
                return iks
            elif customer.priority !=1 and customer.priority ==2:
                print("No VIP found")
                return iks             
            else:
                raise ValueError ("There were no clients at all in the queue")


    @classmethod
    def remove_frist_vip(cls):
        
        iks=cls.search_vip()
        remove_next=cls.client_queue.pop(iks)
        print(f'The removed client is :  {remove_next}')
        
    




BankQueue().add_customer(Customer('Jan Kowalski',1))
BankQueue().add_customer(Customer('Jan Nowak',2))
BankQueue().add_customer(Customer('Tomasz Beble',1))
BankQueue().show_queue()

BankQueue().remove_frist_vip()

BankQueue().show_queue()

BankQueue().remove_frist_vip()
BankQueue().show_queue()

BankQueue().remove_frist_vip()
#BankQueue().show_queue() # There is no more client returned, an error should be returned