from switch import switch

while True:
    print(f"Bienvenido al menu \n")
    try:
        option = int(input("Ingresa el numero del ejercicio: \n 1. Ejercicio 12 \n 2. Ejercicio 15 \n 3. Ejercicio 3 \n 4. Ejercicio 30 \n 5. Ejercicio 17 \n 6. Salir del menu \n\n"))
        if option == 6:
            print("Saliendo del menu")
            break
        else:
            switch(option)
    except:
        print("Ha ingresado un valor invalido \n\n")


