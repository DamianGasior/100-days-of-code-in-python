def calculate_love_score(name1,name2):
    
    name1=name1.lower()
    name2=name2.lower()
    
    
    first_parameter='TRUE'.lower()
    second_parameter='LOVE'.lower()

    
    count_for_true=0
    count_for_love=0

    names=[name1,name2]
    list_of_parameters=[first_parameter,second_parameter]

    for key,parameter in enumerate(list_of_parameters):
        
        for letter_param in parameter:

            for name in names:
                for letter_name in name:
                    if letter_param==letter_name and key==0:
                        count_for_true+=1
                    elif letter_param==letter_name and key==1:
                        count_for_love+=1
    
   

    total_love=str(count_for_true)+str(count_for_love)

    return total_love
                

print(calculate_love_score('Kanye West','Kim Kardashian'))

