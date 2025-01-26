
from sqlite3 import Connection
from typing import Dict, Tuple



class ViagemRepositorios:
    def __init__(self, conexao: Connection) -> None:
        self.__conexao = conexao
        
    def criar_viagem(self, viagem_informações: Dict) -> None: 
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                INSERT INTO TB_VIAGEM (
                    id_viagem, destino_viagem,
                    data_inicio,
                    data_fim,
                    nome_organizador,
                    email_organizador
                ) VALUES (
                    ?, ?, ?, ?, ?, ?
                )
            ''', 
            (
                viagem_informações['id_viagem'],
                viagem_informações['destino_viagem'],
                viagem_informações['data_inicio'],
                viagem_informações['data_fim'],
                viagem_informações['nome_organizador'],
                viagem_informações['email_organizador']
            )
        )
        
        self.__conexao.commit()
        
    def encontrar_viagem_por_id(self, id_viagem: str):
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                SELECT * FROM TB_VIAGEM WHERE id_viagem = ?
            ''', 
            (id_viagem,)
        )
        
        #fetchone só pega uma unica viagem cadastrada no banco
        viagem = cursor.fetchone()
        
        return viagem
    
    
    def mudar_status_viagem(self, id_viagem: str) -> None:
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                UPDATE TB_VIAGEM SET status_viagem = 1 WHERE id_viagem = ?
            ''', 
            (id_viagem,)
        )
        
        self.__conexao.commit()