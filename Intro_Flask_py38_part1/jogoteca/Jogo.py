


class Jogo:
    def __init__(self, nome, categoria, console):
        self.__nome = nome
        self.__categoria = categoria
        self.__console = console

    @property
    def nome(self):
        return self.__nome
    @property
    def categoria(self):
        return self.__categoria
    @property
    def console(self):
        return self.__console