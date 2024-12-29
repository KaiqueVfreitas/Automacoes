import sys 
import os
from controllers.PessoasController import PessoasController
from models.Pessoas import Pessoas
from views.Index import Index



#Adicionando a pasta mae de todo o projeto para facilitar importações
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Função para definir as rotas das controllers e views
def metodo_main():
    print("=== Iniciando o Projeto MVC ===\n")
    
    #Chama a View principal do projeto
    Index()
    
if __name__ == "__main__":
    metodo_main()