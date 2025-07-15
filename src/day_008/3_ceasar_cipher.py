
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



alphabets_length=len(alphabet)#26



def encoding_function(statement,shift_number):
    encoded_statement=''

    
    for letter in statement:
            if letter in alphabet:        
                pos_in_alphabet=alphabet.index(letter)
                print(f'index of letter: "{letter}" is {pos_in_alphabet}')
                encoded_letter=alphabet[(pos_in_alphabet+shift_number)%alphabets_length]
                encoded_statement+=encoded_letter
            else:
                encoded_statement+=letter 
  
    return encoded_statement




def decoding_function(statement,shift_number):
    decoded_statement=''
    for letter in statement:
            if letter in alphabet:
                pos_in_alphabet=alphabet.index(letter)
                print(f'index of letter: "{letter}" is {pos_in_alphabet}')
                decoded_letter=alphabet[(pos_in_alphabet-shift_number)%alphabets_length]
                decoded_statement+=decoded_letter

            else:                               
                decoded_statement+=letter

    return decoded_statement
            

def decision():

    while True:
        action=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if action=='encode' or action=='decode':
            break
        else:
             print('Invalid input, only "encode" or "decode" allowed')

    statement=input('Type your message: ').lower()

    while True:
        users_input=input('Type the shift number equal or greater than 0 : ')
      
        try:
            shift_number = int(users_input)
            if shift_number>=0:
                break
            else:
                print("Number needs to be greater than 0")
        except ValueError:
            print('Insert a valid number')

    if action=='encode':
        print(f'Here is the encoded result: {encoding_function(statement,shift_number)}') 
    elif action=='decode':
        print(f'Here is the encoded result: {decoding_function(statement,shift_number)}') 


decision()

    
 # this 'repeat_statement' needs to be after decision() function , inside the loop so that it asked each time when 'yes'   
while True:
    repeat_statement=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()  
    if repeat_statement=='yes':
        decision()
    else:
        break





