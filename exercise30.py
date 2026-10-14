"""30. Rotación de una lista.
    Crear una lista con ocho números y desplazar sus elementos una
    posición hacia la derecha, haciendo que el último pase a ocupar la
    primera posición.
"""


def ex30():
    list = []

    cantidad = int(input(
            "Ingrese el numero de posiciones que desea en la lista: \n"
        ))

    for i in range (cantidad):
        request = int(input("Ingrese un numero: \n"))
        list.append(request)
        print(f"{list}\n")
        
    last = list.pop()
    list.insert(0, last)

    print(list)

"""
# opción b 
 def ex30():
    list = []
    contador = 0

    cantidad = int(input(
        "Ingrese el numero de posiciones que desea en la lista: \n"
    ))

    for i in range(cantidad):
        request = int(input("Ingrese un numero: \n"))
        list.insert(0, request)
        print(f"\n{list}\n")
 """

"""
opción c
list.reverse()
print(list)
"""