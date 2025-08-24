while True:
    print("\n--BIENVENIDO--")
    print("1.Iniciar sesión")
    print("2.Crear cuenta")
    print("3.Salir")
    option=input("Seleccione una opción (1-3): ")

    #Opcion=registro()
    match option:
        case "1":
            #opcion.ingresar_cajero()
            while True:
                print("\n--MENÚ--")
                print("1.Consultar cuenta")
                print("2.Retirar")
                print("3.Cambiar PIN")
                print("4.Historial de Transacciones")
                print("5.Salir\n")
                option2 = input("Seleccione una opción (1-5):")

                match option2:
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
                        print("Ocurrió un error inesperado")
        case "2":
            print()
        case "3":
            print("Gracias por usar el programa")
            break
        case _:
            print("Error inesperado, inténtelo de nuevo")

