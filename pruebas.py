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
        self.cuentas = {}

    def crear_cuenta(self, numero_cuenta, nombre, pin, saldo):
        if numero_cuenta in self.cuentas:
            raise ValueError("El número de cuenta ya existe")
        if saldo <= 0:
            raise ValueError("El saldo no puede ser menor o igual a 0")

        self.cuentas[numero_cuenta] = {
            "pin": pin,
            "info": {
                "nombre": nombre,
                "saldo": saldo
            }
        }

    def mostrar_info(self, numero_cuenta, pin_ingresado):
        if numero_cuenta not in self.cuentas:
            print("Cuenta no encontrada.")
            return

        cuenta = self.cuentas[numero_cuenta]

        if cuenta["pin"] == pin_ingresado: # validar si es el pin del numero de cuenta
            print(f"\nBienvenido {cuenta['info']['nombre']}")
            print(f"Saldo actual Q: {cuenta['info']['saldo']}")
        else:
            print("PIN incorrecto. Acceso denegado.")

# Comprobando si funciona
registro = Registro()
registro.crear_cuenta("1234", "Cristhian", "333", 777)
registro.crear_cuenta("12345", "Diego", "123", 1000)
registro.crear_cuenta("123456", "Santiago", "777", 750.50)

numero = input("Ingrese número de cuenta: ")
pin = input("Ingrese su PIN: ")

registro.mostrar_info(numero, pin)
# Si da así