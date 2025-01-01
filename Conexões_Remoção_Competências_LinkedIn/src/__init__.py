
#Este codigo só funciona no python 3.10.0 ou superior
import sys
import os

#Imports usados para acessar arquivos nos tests
from src.views.Index import Index
from src.views.Menu import Menu
from src.controllers.MenuController import MenuController
from src.controllers.LinkedinController import LinkedinController
from src.models.Linkedin import Linkedin

#Adicionando a pasta mae de todo o projeto para facilitar importacoes
sys.path.append("..")



if sys.version_info < (3, 10):
    raise Exception("Este codigo funciona no python 3.10.0 ou superior")
else:
    print("Versão correta do python")
    
#verifica se as bibliotecas estao instaladas
try:
    print("Todas as bibliotecas necessárias estão instaladas.")
except ImportError as e:
    print(f"Biblioteca ausente: {e.name}. Instale com 'pip install -r requirements.txt'.")