""" 
Invertir un número entero positivo: Solicita al usuario un número entero positivo y utiliza operaciones matemáticas, 
junto con un ciclo `while`, para extraer sus dígitos y formar el número en orden inverso.
Finalmente, muestra el número invertido en pantalla.
"""
def ex17():
    numero = int(input("Ingresa un número entero positivo: "))

    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10

    print("Numero invertido:", invertido)