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

class Registro:
    def __init__(self):
        self.diccionario = {}

    def crear_cuenta(self):
        nombre = input("Ingrese su nombre: ")
        numero_cuenta = input("Ingrese el número de cuenta que quiera tener: ")
        pin = input("Escriba el pin de su cuenta: ")
        saldo = int(input("Ingrese la cantidad de dinero que va a tener su cuenta: "))
        self.diccionario[numero_cuenta] = Cuenta(nombre,numero_cuenta, pin, saldo)

