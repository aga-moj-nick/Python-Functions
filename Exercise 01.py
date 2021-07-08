# 1. Write a Python function to find the Max of three numbers.


def maks_z_trzech (a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c
    
print (maks_z_trzech (5, 10, 15))
