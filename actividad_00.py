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
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
        else:
            print("El saldo no puede ser menor a Q0\n")

    def mostrar_info(self):
        return f"\nNúmero de cuenta: {self.numero_cuenta} - Saldo: Q{self.saldo}\n"

    def sett_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    @property
    def pin(self):
        return self.__pin

    def cambiar_pin(self):
        while True:
            try:
                pin_actual = input("Ingrese el PIN actual: ").strip()
                if not pin_actual:
                    raise ValueError("El PIN actual no puede estar vacío")
                if pin_actual != self.__pin:
                    raise ValueError("PIN incorrecto")

                nuevo_pin = input("Ingrese el nuevo PIN: ").strip()
                if not nuevo_pin:
                    raise ValueError("El nuevo PIN no puede estar vacío")
                if nuevo_pin == self.__pin:
                    raise ValueError("El nuevo PIN no puede ser igual al anterior")

                self.__pin = nuevo_pin
                print(f"Se ha cambiado el PIN. Nuevo PIN guardado: {nuevo_pin}")
                break

            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.\n")

    def mostrar_historial(self):
        if not self._historial_retiros:
            print("No hay retiros registrados.\n")
        else:
            print("\nHistorial de retiros:")
            for retiro in self._historial_retiros:
                print(f"- Retiro de Q{retiro}")

class Registro:
    def __init__(self):
        self.diccionario = {112233: Cuenta("Manuel", 112233, "1234", 5000),
            192837: Cuenta("Silvia", 192837, "5678", 7500),
            987654: Cuenta("Carlos", 987654, "9012", 250)}

    def crear_cuenta(self):

        while True:
            try:
                numero_cuenta_input = input("Ingrese el numero de cuenta: ")
                if not numero_cuenta_input.strip():
                    raise ValueError("No puede dejar el número de cuenta vacío\n")
                numero_cuenta = int(numero_cuenta_input)
                if numero_cuenta <= 0:
                    raise ValueError("El número de cuenta debe ser mayor que 0\n")
                if numero_cuenta in self.diccionario:
                    raise ValueError("La cuenta ya existe\n")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break

        while True:
            try:
                pin = input("Ingrese el PIN de la cuenta: ")
                if not pin.strip():
                    raise ValueError("No puede dejar el PIN vacío\n")
            except ValueError as e:
                print(f"Error: {e}\n")
            else:
                break

        while True:
            try:
                nombre = input("Ingrese el nombre de la cuenta: ")
                if not nombre.strip():
                    raise ValueError("No puede dejar el nombre vacío\n")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                break

        while True:
            try:
                saldo_input = input("Ingrese el saldo de la cuenta Q: ")
                if not saldo_input.strip():
                    raise ValueError("No puede dejar el saldo vacío\n")
                saldo = float(saldo_input)
                if saldo <= 0:
                    raise ValueError("El saldo debe ser mayor que Q0\n")

            except Exception as e:
                print(f"Error: {e}")

            else:
                break

        self.diccionario[numero_cuenta] = Cuenta(nombre, numero_cuenta, pin, saldo)
        print(f"Cuenta creada con exito")

    def ingresar_cajero(self):
        try:
            numero_cuenta_input = input("Ingrese el número de cuenta: ")
            if not numero_cuenta_input.strip():
                raise ValueError("No puede dejar vacío el número de cuenta\n")
            numero_cuenta = int(numero_cuenta_input)
        except Exception as e:
            print(f"Error: {e}")
            return None

        cuenta = self.diccionario.get(numero_cuenta)
        if not cuenta:
            print("Cuenta no encontrada.\n")
            return None

        try:
            pin_cuenta = input("Ingrese el PIN de la cuenta: ")
            if not pin_cuenta.strip():
                raise ValueError("No puede dejar vacío el PIN\n")
        except ValueError as e:
            print(f"Error: {e}")
            return None

        if cuenta.sett_pin(pin_cuenta):
            print(f"\nBienvenido, {cuenta.nombre}.")
            return cuenta

        print("Pin incorrecto.\n")
        return None

    def retirar(self, cuenta):
        try:
            monto_cuenta = input("Ingrese la cantidad a retirar: Q")
            if not monto_cuenta.strip():
                raise ValueError("No puede dejar vacío el monto a retirar\n")

            monto = float(monto_cuenta)
            if monto <= 0:
                print("El monto debe ser positivo.\n")
                return
            if monto > cuenta.saldo:
                print("Fondos insuficientes\n")
                return

            cuenta.saldo = cuenta.saldo - monto
            cuenta._historial_retiros.append(monto)
            print(f"El nuevo saldo es de Q{cuenta.saldo}\n")
            print()
        except Exception as e:
            print(f"Error inesperado: {e}")

    def consultar_cuenta(self, cuenta):
        print(cuenta.mostrar_info())

registro=Registro()

while True:
    print("\n--BIENVENIDO--")
    print("1.Iniciar sesión")
    print("2.Crear cuenta")
    print("3.Salir\n")
    option=input("Seleccione una opción (1-3): ")


    match option:
        case "1":
            cuenta = registro.ingresar_cajero()
            if cuenta is None:
                continue
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
                        registro.consultar_cuenta(cuenta)
                    case "2":
                        registro.retirar(cuenta)
                    case "3":
                        cuenta.cambiar_pin()
                    case "4":
                        cuenta.mostrar_historial()
                    case "5":
                        print("Gracias por usar el programa.")
                        break
                    case _:
                        print("Ocurrió un error inesperado\n")
        case "2":
            registro.crear_cuenta()
        case "3":
            print("Gracias por usar el programa")
            break
        case _:
            print("Error inesperado, inténtelo de nuevo\n")

#Cuentas quemadas:
#112233: Cuenta("Manuel", 112233, "1234", 5000),
#192837: Cuenta("Silvia", 192837, "5678", 7500),
#987654: Cuenta("Carlos", 987654, "9012", 250)