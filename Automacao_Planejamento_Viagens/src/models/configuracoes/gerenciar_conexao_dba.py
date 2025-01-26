import sqlite3
from sqlite3 import Connection

class GerenciarConexaoDBA:
    def __init__(self) -> None:
        self.__string_conexao_banco_dados = "dbPlanejamentoViagens"
        self.__conexao = None
        
    def conectar_banco_dados(self) -> None:
        conexao = sqlite3.connect(self.__string_conexao_banco_dados, check_same_thread=False)
        
        self.__conexao = conexao
        
    def get_conexao(self) -> Connection:
        return self.__conexao

gerenciar_conexao_dba = GerenciarConexaoDBA()