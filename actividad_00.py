class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo):
        self.numero_cuenta = numero_cuenta
        self.__pin = pin
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo