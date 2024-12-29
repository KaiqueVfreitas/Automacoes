class Pessoas:
    def __init__(self, nome: str, sobrenome: str, idade: int, cpf: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
    def metodo_nome_completo(self):
        return self.nome + self.sobrenome 