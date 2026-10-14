from ejercicio12 import ex12
from exercise30 import ex30
from exercise15 import ex15
from exercise17 import ex17
from exercise26 import ex26


def switch(a):
    if a == 1:
        print(f"Ejercicio 12: \n")
        ex12()
    elif a == 2:
        print("Ejercicio 15: \n")
        ex15()
    elif a == 3:
        print("Ejercicio 26: \n")
        ex26()
    elif a == 4:
        print("Ejercicio 30: \n")
        ex30()
    elif a == 5:
        print("Ejercicio 17: \n")
        ex17()
    else:
        print("Ha seleccionado una opción diferente a las disponibles")