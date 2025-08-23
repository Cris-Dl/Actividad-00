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

    def crear_cuenta(self):

        while True:
            try:
                numero_cuenta = int(input("Ingrese el numero de cuenta: "))
                if not numero_cuenta:
                    raise ValueError("No puede dejar el numero de cuenta esto vacío")

                if numero_cuenta <= 0:
                    raise ValueError("No puede dejar el numero de cuenta en 0")

                if numero_cuenta in self.cuentas:
                    raise ValueError("El cuenta ya existe en la lista")

            except Exception as e:
                print(f"Error inesperado: {e}")

            else:
                break

        while True:
            try:
                pin = input("Ingrese el pin de la cuenta: ")
                if not pin:
                    raise ValueError("No puede dejar el PIN vacío")

            except ValueError:
                print("Error: El pin no es valido, intente de nuevo")

            else:
                break

        while True:
            try:
                nombre = input("Ingrese el nombre de la cuenta: ")
                if not nombre:
                    raise ValueError("No puede dejar el nombre vacío")

            except Exception as e:
                print(f"Error inesperado: {e}")
            else:
                break

        while True:
            try:
                saldo = float(input("Ingrese el saldo de la cuenta Q: "))
                if saldo <= 0:
                    raise ValueError("Saldo no puede ser menor o igual a 0")

            except ValueError:
                print("Error: El valor de saldo no es valido, intente de nuevo")

            except Exception as e:
                print(f"Error inesperado: {e}")

            else:
                break

        self.cuentas[numero_cuenta] = {
            "pin": pin,
            "info": {
                "nombre": nombre,
                "saldo": saldo
                }
            }
        print("Cuenta creada con exito")

registro = Registro()
registro.crear_cuenta()