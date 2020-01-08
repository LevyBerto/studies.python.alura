class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__cd_banco = '001'

    def extrato(self):
        print("Saldo é {} do titular \"{}\"".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_sacar):
        valor_disponivel = self.saldo + self.limite
        return valor_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar():
            self.__saldo -= valor
        else:
            print("O valor {} passou o limmite".format(valor))

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite()

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod # Retorna um atributo estatico sem a necessidade de instanciar um objeto.
    def cd_banco():
        return '001'

    @staticmethod # Retorna um atributo estatico sem a necessidade de instanciar um objeto.
    def cd_bancos():
        return {"BB": '001', "Caixa": '104', "Bradesco":'237'}