# 19. Write a Python program to access a function inside a function.

def liczba (a):
        def druga_liczba (b):
                nonlocal a
                a += 1
                return a + b
        return druga_liczba

funkcja = liczba (5)
print (funkcja (5))



