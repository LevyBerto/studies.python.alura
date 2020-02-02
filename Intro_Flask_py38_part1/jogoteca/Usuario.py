class Usuario:
    def __init__(self, id, nome, senha):
        self.__id = id
        self.__nome = nome.title()
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @property
    def senha(self):
        return self.__senha
