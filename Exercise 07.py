# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


string = 'abcDEF'

def obliczanie (string):
    return len (string)


def obliczanie_duże (string):
    return sum (1 for i in string if i.isupper ()) 
   

def obliczanie_małe (string):
    return sum (1 for i in string if i.islower ())



print ("Wszystkich liter jest: ", obliczanie (string))
print ("Dużych liter jest: ", obliczanie_duże (string))
print ("Małych liter jest: ", obliczanie_małe (string))



