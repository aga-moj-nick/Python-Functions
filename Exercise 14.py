# 14. Write a Python function to check whether a string is a pangram or not. 


def pangram (str):
    alfabet =  'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    for literka in alfabet:
       if literka not in str.lower():
           return False

       else:
        continue
    
    return True



zdanie = 'Filmuj rzeź żądań, pość, gnęb chłystków!'

if (pangram (zdanie) == True):
    print ('Pangram')
else:
    print ('Nie pangram')
