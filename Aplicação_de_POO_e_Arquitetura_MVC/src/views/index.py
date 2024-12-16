import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controllers.PessoasController import PessoasController
from models.Pessoas import Pessoas


decisao = int(input("Digite 1 para salvar ou 2 para listar: "))

while True:
    if decisao == 1:
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o cpf: ")
        p1 = Pessoas(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoasController.metodo_salvar_pessoas(p1)
    elif decisao == 2:
        for i in PessoasController.metodo_listar_pessoas():
            print(f"Nome: {i.nome}")
    else:
        print("Opção inválida")