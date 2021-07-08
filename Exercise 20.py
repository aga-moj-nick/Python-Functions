# 20. Write a Python program to detect the number of local variables declared in a function.


def zmienne():
   a = 25.5
   b = 5
   str_ = 'cośtamcośtam'

print("Liczba zmiennych lokalnych to: ", zmienne.__code__.co_nlocals)
