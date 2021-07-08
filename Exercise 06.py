# 6. Write a Python function to check whether a number falls in a given range. 

liczba = int (input ("Podaj liczbę: "))

def sprawdzanie (liczba):
    if liczba in range (0, 10):
        return (0, 10)


print ("Zgadłeś!Zgadywany zakres to:  ", sprawdzanie (liczba))
