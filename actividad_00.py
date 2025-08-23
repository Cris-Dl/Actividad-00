class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo):
        self.numero_cuenta = numero_cuenta
        self.__pin = pin
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def mostrar_info(self):
        return f"Número de cuenta:{self.numero_cuenta} - Saldo: {self.saldo}"

class Registro:
    def __init__(self):
        self.diccionario = {}

    def crear_cuenta(self):
        nombre = input("Ingrese el nombre del cliente: ")