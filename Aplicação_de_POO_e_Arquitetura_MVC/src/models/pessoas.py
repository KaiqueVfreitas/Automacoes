class Pessoas:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__cpf = cpf
    def nome_completo(self):
        return self.nome + self.sobrenome 