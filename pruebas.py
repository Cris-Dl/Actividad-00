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
                numero_cuenta_input = input("Ingrese el numero de cuenta: ")
                if not numero_cuenta_input.strip():
                    raise ValueError("No puede dejar el número de cuenta vacío")
                numero_cuenta = int(numero_cuenta_input)
                if numero_cuenta <= 0:
                    raise ValueError("El número de cuenta debe ser mayor que 0")
                if numero_cuenta in self.cuentas:
                    raise ValueError("La cuenta ya existe")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break

        while True:
            try:
                pin = input("Ingrese el PIN de la cuenta: ")
                if not pin.strip():
                    raise ValueError("No puede dejar el PIN vacío")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break

        while True:
            try:
                nombre = input("Ingrese el nombre de la cuenta: ")
                if not nombre.strip():
                    raise ValueError("No puede dejar el nombre vacío")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break

        while True:
            try:
                saldo_input = input("Ingrese el saldo de la cuenta Q: ")
                if not saldo_input.strip():
                    raise ValueError("No puede dejar el saldo vacío")
                saldo = float(saldo_input)
                if saldo <= 0:
                    raise ValueError("El saldo debe ser mayor que 0")

            except Exception as e:
                print(f"Error: {e}\n")

            else:
                break

        self.cuentas[numero_cuenta] = {
            "pin": pin,
            "info": {
                "nombre": nombre,
                "saldo": saldo
                }
            }
        print(f"\nCuenta '{numero_cuenta}' creada con exito\n")