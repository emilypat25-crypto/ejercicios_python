#Suma de números naturales. Solicitar un número N y calcular la suma de todos los enteros desde 1 hasta N.
#Entrada y salida: utilizar input() para solicitar información y print() para mostrar los resultados cuando sea necesario.

def ex12():
    N = int(input("Ingrese un número natural: "))
    suma = 0
    for i in range(1, N + 1):
        suma += i
    print("La suma de los números naturales desde 1 hasta", N, "es:", suma)

if __name__ == "__main__":
    ex12()