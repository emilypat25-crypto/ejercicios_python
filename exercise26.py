"""Ejercicio 26: Ordenar 10 números de menor a mayor (burbuja), sin sort()
ni sorted().
"""


def pedir_numeros(cantidad):
    """Pide 'cantidad' números por teclado y devuelve la lista con ellos."""
    numeros = []
    while len(numeros) < cantidad:
        texto = input(
            f"Ingresa el número {len(numeros) + 1} de {cantidad}: "
        )
        try:
            numeros.append(float(texto) if "." in texto else int(texto))
        except ValueError:
            print("  Entrada no válida. Escribe un número (ej: 7, -3, 2.5).")
    return numeros


def ordenar_burbuja(lista):
    """Ordena la lista de menor a mayor, modificándola en el lugar."""
    n = len(lista)
    for i in range(n - 1):              # máximo n-1 pasadas
        hubo_intercambio = False
        for j in range(n - 1 - i):      # los últimos i ya están en su sitio
            if lista[j] > lista[j + 1]:  # comparación
                temporal = lista[j]      # intercambio con variable temporal
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
                hubo_intercambio = True
        if not hubo_intercambio:        # si no hubo cambios, ya está ordenada
            break
    return lista


def esta_ordenada(lista):
    """Devuelve True si cada elemento es menor o igual que el siguiente."""
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def ex26():
    """Función que llama el menú."""
    numeros = pedir_numeros(10)
    print("\nLista original:", numeros)
    ordenar_burbuja(numeros)
    print("Lista ordenada:", numeros)
    print("¿Está ordenada?", esta_ordenada(numeros))
    print()


if __name__ == "__main__":
    ex26()