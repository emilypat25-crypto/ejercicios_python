from exercise30 import ex30
from exercise15 import ex15
from exercise17 import ex17

def switch (a):
    if a == 1:
        print(f"Ejercicio 12: \n")
    elif a == 2:
        print(f"Ejercicio 15: \n")
        ex15()
    elif a == 3:
        print(f"Ejercicio 3: \n")
    elif a == 4:
            print(f"Ejercicio 30: \n")
            ex30()
    elif a == 5:
        print("Ejercicio 17: \n")
        ex17()        
    else:
        print("Ha seleccionado una opción diferente a las disponibles")