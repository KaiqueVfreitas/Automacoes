from typing import List
from models import Pessoas

class PessoasController:
    _pessoas = []  
    
    @classmethod
    def metodo_salvar_pessoa(cls) -> None:
        print("\n=== Cadastrar Pessoa ===")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        try:
            idade = int(input("Digite a idade: "))
        except ValueError:
            print("Erro: Idade inválida!")
            return
        cpf = input("Digite o CPF: ")

        pessoa = Pessoas(nome, sobrenome, idade, cpf)
        cls._pessoas.append(pessoa)
        print("Pessoa salva com sucesso!")

    @classmethod
    def metodo_listar_pessoas(cls) -> None:
        print("\n=== Lista de Pessoas Cadastradas ===")
        if not cls._pessoas:
            print("Nenhuma pessoa cadastrada até o momento.")
            return
        
        for pessoa in cls._pessoas:
            print(f"Nome: {pessoa.metodo_nome_completo()}, Idade: {pessoa.idade}, CPF: {pessoa.cpf}")
            