class Cliente():

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print(self.__nome)

    @nome.setter
    def nome(self, nn):
        self.__nome = nn
        print("Mudei")