# 14. Write a Python function to check whether a string is a pangram or not. 


def pangram (str):
    alfabet =  'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    for literki in alfabet:
       if literki not in str.lower(alfabet):
           return False

       else:
            return True



string = 'Filmuj rzeź żądań, pość, gnęb chłystków!'

if (pangram (str) == True):
    print ('Pangram')
else:
    print ('Nie pangram')
