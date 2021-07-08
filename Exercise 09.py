# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.


liczba = int (input ("Podaj liczbę: "))


def sprawdzanie (liczba):
    if liczba <= 1:
        return False
    if liczba > 1:
        return True
print (sprawdzanie (liczba))
