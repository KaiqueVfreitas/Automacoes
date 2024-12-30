import sys 
import os
from controllers import LinkedinController
from models import Linkedin
from views import Index
from views import Menu



#Adicionando a pasta mae de todo o projeto para facilitar importações
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Função para definir a view inicial
def metodo_main():
    print("=== Iniciado o Projeto Conexões e Remoção de Competências no LinkedIn ===\n")
    
    #Chama a View principal do projeto
    Index()
    
if __name__ == "__main__":
    metodo_main()