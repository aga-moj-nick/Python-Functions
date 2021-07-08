# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


stringi = input ("Podaj trzy słówka: ")

def sortowanie (stringi):
    
    łącznik = stringi.split ()
    łącznik.sort ()
    return ('-'.join (łącznik))

print (sortowanie (stringi))
    
