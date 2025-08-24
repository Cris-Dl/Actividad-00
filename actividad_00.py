class Cuenta:
    def __init__(self, nombre, numero_cuenta, pin, saldo):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
        self.__pin = pin
        self._saldo = saldo
        self._historial_retiros = []

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

    @property
    def pin(self):
        return self.__pin

    def cambiar_pin(self):
        pin_actual = input("Ingrese el pin actual: ")
        if self.__pin != pin_actual:
            print(" Pin incorrecto")
            return
        nuevo_pin = input("Ingrese el nuevo pin: ")
        if nuevo_pin == self.__pin:
            print("El nuevo pin no puede ser igual al anterior.")
            return
        self.__pin = nuevo_pin
        print(f" Se ha cambiado el pin. Nuevo pin guardado {nuevo_pin}.")

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
        cuenta = self.diccionario[numero_cuenta]
        if cuenta.sett_pin(pin_cuenta):
            print(f"Bienvenido, {cuenta.nombre}")
            return cuenta
        print(" Pin incorrecto.")
        return None

    def retirar(self, cuenta):
        monto = int(input("Ingrese la cantidad a retirar: "))
        if monto <= 0:
            print(" El monto debe ser positivo.")
            return
        if monto > cuenta.saldo:
            print(" Fondos insuficientes.")
            return
        cuenta.saldo = cuenta.saldo - monto
        cuenta._historial_retiros.append(monto)
        print(f"El nuevo saldo es de {cuenta.saldo}")
        print()

    def consultar_cuenta(self, cuenta):
        print(cuenta.mostrar_info())
