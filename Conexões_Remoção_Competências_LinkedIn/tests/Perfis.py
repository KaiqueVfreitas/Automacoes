import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importa a classe Menu para realizar testes
from views.Menu import Menu

# Exemplo de teste
if __name__ == "__main__":
    # Instancia a interface do Menu
    menu = Menu()
    print("Interface do Menu aberta com sucesso!")
