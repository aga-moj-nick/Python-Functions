# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


n = int (input ("Podaj nieujemną liczbę całkowitą: "))


def silnia(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * silnia (n - 1)
  
 

print ("Silnia to: ", silnia(n))
 
