def first_number_function():
    while True:
        first_number=(input('What is yor first number ?:'))   
        try:
            f_number=float(first_number)
            return f_number
        
        except ValueError:
            print('Insert a valid symbol')
           
f_number=first_number_function()


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2




def operator_function():
    while True:
        operation_symbol=''
        print(
    r'''
    +
    -
    *
    /''')
        operation_input=input('Pick an operation:').strip()
        if operation_input =='+':
            operation_type_function_function=add
            operation_symbol='+'
            return operation_type_function_function,operation_symbol 
        elif operation_input=='*':
            operation_type_function=multiply
            operation_symbol='*'
            return operation_type_function,operation_symbol 
        elif operation_input=='/':
            operation_type_function=divide
            operation_symbol='/'
            return operation_type_function,operation_symbol 
        elif operation_input=='-':
            operation_type_function=subtract
            operation_symbol='-'
            return operation_type_function,operation_symbol 
        else:
            print('Insert a valid symbol')

operation_type_function,operation_symbol=operator_function()
#print(operation_symbol)


def second_number_function():
    while True:
        second_number=(input('What is the second number?: '))   
        try:
            s_number=float(second_number)
            return s_number
        
        except ValueError:
            print('Insert a valid symbol')
  
s_number=second_number_function()


def final_operation():
    result=operation_type_function(f_number,s_number)
    print(f'{f_number} {operation_symbol} {s_number} = {result}')
    return result

result=final_operation()


while True:
    next_steps=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, type 'q' to exit the program: ").lower()
    if next_steps=='y':
        f_number=result
        operation_type_function,operation_symbol=operator_function()
        s_number=second_number_function()
        result=final_operation()
    elif next_steps=='n':
        f_number=first_number_function()
        operation_type_function,operation_symbol=operator_function()
        s_number=second_number_function()
        result=final_operation()
    elif next_steps=='q':
        print('Thank you for using this simple calculator')
        break
 




