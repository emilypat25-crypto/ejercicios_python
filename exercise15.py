""" 
Serie Fibonacci. Solicitar cuántos términos desea visualizar el usuario y generar la secuencia comenzando por 0 y 1.
"""
def ex15 ():

    while True:
        try:
            n = int(input("¿Cuántos términos deseas visualizar? "))

            if n <= 0:
                print("Error: ingresa un número mayor a 0")
                continue

            a = 0
            b = 1

            for i in range(n):
                print(a)
                c = a + b
                a = b
                b = c

        except ValueError:
            print("Error: debes ingresar un número entero")
            continue

        while True:
            salir = input("¿Deseas salir? Escribe si o no: ").lower()

            if salir == "si":
                print("Programa finalizado")
                break
            elif salir == "no":
                break
            else:
                print("Respuesta incorrecta. Escribe si o no.")

        if salir == "si":
            break
