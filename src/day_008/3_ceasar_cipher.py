import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(len(alphabet)) #26
alphabets_len=len(alphabet)
adj_alphabets_len=len(alphabet)-1


def encoding_function(statement,shift_number):
    encoded_statement=''

    
    for i in statement:
        if i in alphabet:
            pos_in_alphabet=alphabet.index(i)
            print(f'index of letter: "{i}" is {pos_in_alphabet}')
            max_range=pos_in_alphabet+shift_number
            if max_range<=adj_alphabets_len and shift_number>=0: 
                encoded_letter=alphabet[pos_in_alphabet+shift_number]
                encoded_statement+=encoded_letter


            elif max_range>adj_alphabets_len and shift_number>0: 
                new_index=(pos_in_alphabet+shift_number)%alphabets_len
                encoded_letter=alphabet[new_index]
                encoded_statement+=encoded_letter
            else:
                encoded_statement+=i  
        else:
            encoded_statement+=i

    return encoded_statement




def decoding_function(statement,shift_number):
    decoded_statement=''
    for i in statement:
            if i in alphabet:
                pos_in_alphabet=alphabet.index(i)
                print(f'index of letter: "{i}" is {pos_in_alphabet}')
                min_lenght=pos_in_alphabet+shift_number 
                if min_lenght >= 0 and shift_number>=0:
                    new_index=pos_in_alphabet-shift_number 
                    decoded_letter=alphabet[new_index]
                    decoded_statement+=decoded_letter
                             
                elif min_lenght < 0 and shift_number>0:
                    new_index=alphabets_len-abs(pos_in_alphabet-shift_number)
                    decoded_letter=alphabet[new_index]
                    decoded_statement+=decoded_letter

                else:                               
                    decoded_statement+=i
            else:                               
                    decoded_statement+=i 

    return decoded_statement
            

def decision():
    action=input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
    statement=input('Type your message: ').lower()
    shift_number=int(input('Type the shift number: '))

    if action=='encode':
        print(f'Here is the encoded result: {encoding_function(statement,shift_number)}') 
    elif action=='decode':
        print(f'Here is the encoded result: {decoding_function(statement,shift_number)}') 


decision()

repeat_statement=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()   
    
    
while True:
   
    if repeat_statement=='yes':
        decision()
    else:
        break





