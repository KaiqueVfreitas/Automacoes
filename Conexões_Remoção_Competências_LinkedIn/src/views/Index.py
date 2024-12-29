import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controllers import PessoasController


class Index:
    def __init__(self):
        self.metodo_menu_principal()

    def metodo_menu_principal(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Cadastrar Pessoa")
            print("2. Listar Pessoas")
            print("3. Sair")

            try:
                decisao = int(input("Digite sua escolha: "))
                if decisao == 1:
                    PessoasController.metodo_salvar_pessoa()
                elif decisao == 2:
                    PessoasController.metodo_listar_pessoas()
                elif decisao == 3:
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Erro: Por favor, digite apenas números.")
