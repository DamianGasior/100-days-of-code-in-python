def input_from_user(users_input):
    while True:
        try:
            number=float(input(users_input))
            return number
        except ValueError:
            print('Insert a valid entry')


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
            operation_type_function=add
            operation_symbol='+'
            return operation_type_function,operation_symbol 
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




def calculate_and_print(f_number,s_number,operation_type_function,operation_symbol ):
    result=operation_type_function(f_number,s_number)
    print(f'{f_number} {operation_symbol} {s_number} = {result}')
    return result




def last_question(result,f_number,s_number,operation_type_function,operation_symbol):
    while True:
        next_steps=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, type 'q' to exit the program: ").lower()
        if next_steps=='y':
            f_number=result
            operation_type_function,operation_symbol=operator_function()
            s_number=input_from_user('What is your second  number ?:')
            result=calculate_and_print(f_number,s_number,operation_type_function,operation_symbol)
        elif next_steps=='n':
            f_number=input_from_user('What is your first number ?:')
            operation_type_function,operation_symbol=operator_function()
            s_number=input_from_user('What is your second  number ?:')
            result=calculate_and_print(f_number,s_number,operation_type_function,operation_symbol)
        elif next_steps=='q':
            print('Thank you for using this simple calculator')
            return next_steps
            






def main():

    f_number=input_from_user('What is your first number ?:')
    operation_type_function,operation_symbol=operator_function()
    s_number=input_from_user('What is your second  number ?:')
    result=calculate_and_print(f_number,s_number,operation_type_function,operation_symbol)
    last_question(result,f_number,s_number,operation_type_function,operation_symbol)


if __name__=="__main__":
    main()
    



