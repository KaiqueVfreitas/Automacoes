class Pessoas:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
    def nome_completo(self):
        return self.nome + self.sobrenome 