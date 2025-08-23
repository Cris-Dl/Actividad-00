while True:
    print("\n--MENÚ--")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("5.Salir\n")
    option=input("Seleccione una opción (1-5):")

    match option:
        case "1":
            print()
        case "2":
            print()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Ocurrió un error inesperado, inténtelo de nuevo.")