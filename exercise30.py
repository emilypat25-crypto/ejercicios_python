"""30. Rotación de una lista.
    Crear una lista con ocho números y desplazar sus elementos una
    posición hacia la derecha, haciendo que el último pase a ocupar la
    primera posición.
"""


def ex30():
    list = []
    contrado = 0

    cantidad = int(input(
        "Ingrese el numero de posiciones que desea en la lista: \n"
    ))

    for i in range(cantidad):
        request = int(input("Ingrese un numero: \n"))
        list.insert(contrador, request)
        contrado = contrado - 1
        print(f"\n{list}\n")


"""
opción b
list.reverse()
print(list)
"""