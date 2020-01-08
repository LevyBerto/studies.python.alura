
class Cliente:

    def __init__(self, nome):
        print("Construindo Cliente... {}".format(self))
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter #define um setter para a @propriedade nome()
    def nome(self, nome):
        print("Chamando @nome.setter nome()")
        self.__nome = nome

