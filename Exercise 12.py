# 12. Write a Python function that checks whether a passed string is palindrome or not.


palindrom = str (input ("Podaj słowo: "))


def sprawdzanie (palindrom):
    palindrom2 = palindrom [: : -1]
    if palindrom2 == palindrom:
        return palindrom
    else:
        return False

print ("To słowo jest palindromem.", sprawdzanie (palindrom))
    
