# 10. Write a Python program to print the even numbers from a given list.



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def parzyste (lista):
    lista_parzystych = []
    for liczba in lista:
        if (liczba % 2 == 0):
            lista_parzystych.append (liczba)
    return lista_parzystych
        

print (parzyste (lista))



