class Cuenta:
    def __init__(self, nombre, numero_cuenta, pin, saldo):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.__pin = pin
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo > 0:
            self._saldo = nuevo_saldo
        else:
            print("El saldo no puede ser menor o igual a 0")

    def mostrar_info(self):
        return f"Número de cuenta:{self.numero_cuenta} - Saldo: {self.saldo}"

    def sett_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

class Registro:
    def __init__(self):
        self.diccionario = {}

    def crear_cuenta(self):
        nombre = input("Ingrese su nombre: ")
        numero_cuenta = input("Ingrese el número de cuenta que quiera tener: ")
        pin = input("Escriba el pin de su cuenta: ")
        saldo = int(input("Ingrese la cantidad de dinero que va a tener su cuenta: "))
        self.diccionario[numero_cuenta] = Cuenta(nombre,numero_cuenta, pin, saldo)

    def ingresar_cajero(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        pin_cuenta = input("Ingrese el pin de la cuenta: ")
        if numero_cuenta not in self.diccionario:
            print("Cuenta no encontrada")

        cuenta = self.diccionario[numero_cuenta]
        if cuenta["pin"] == pin_cuenta:
            print(f"Bienvenido")

    def deposito(self, cuenta):
        monto = int(input("Ingrese el monto a depositar: "))
        cuenta.saldo = cuenta.saldo + monto
        print("Se ha realizado el deposito")

op1=Registro()

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
            op1.crear_cuenta()
        case "2":
            op1.deposito()
        case "3":
            print()
        case "4":
            print()
        case "5":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Ocurrió un error inesperado, inténtelo de nuevo.")