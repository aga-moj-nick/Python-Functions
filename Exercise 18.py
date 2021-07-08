# 18. Write a Python program to execute a string containing Python code. 



hasło = "print ('Python')"
drugie_hasło = """
def mnożenie (a, b):
    return a * b

print ('Wynik mnożenia to: ', mnożenie (2, 5))
"""


exec(hasło)
exec(drugie_hasło)


