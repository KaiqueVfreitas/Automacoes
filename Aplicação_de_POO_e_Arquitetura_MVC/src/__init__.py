#Este codigo só funciona no python 3.10.0 ou superior
import sys

if sys.version_info < (3, 10):
    raise Exception("Este codigo funciona no python 3.10.0 ou superior")
else:
    print("Versão correta do python")
    
#verifica se as bibliotecas estao instaladas
try:
    import colorama
    import pytest
    print("Todas as bibliotecas necessárias estão instaladas.")
except ImportError as e:
    print(f"Biblioteca ausente: {e.name}. Instale com 'pip install -r requirements.txt'.")