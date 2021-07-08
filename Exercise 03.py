# 3. Write a Python function to multiply all the numbers in a list.


import math

lista = [1, 2, 3]

def mnożenie (lista):
    liczba = 1
    for i in lista:
        liczba *= i
    return liczba

print (mnożenie (lista))
