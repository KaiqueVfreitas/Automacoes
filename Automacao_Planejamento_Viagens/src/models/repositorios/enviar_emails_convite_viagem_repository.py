
from sqlite3 import Connection
from typing import Dict, List, Tuple



class EnviarEmailsConviteViagemRepository:
    def __init__(self, conexao: Connection) -> None:
        self.__conexao = conexao
        
    def registrar_emails_participantes(self, emails_informacoes: Dict) -> None: 
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                INSERT INTO TB_ENVIO_CONVITE (
                    id_envio_convite, email_envio, id_viagem
                ) VALUES (
                    ?, ?, ?
                )
            ''', 
            (
                emails_informacoes['id_envio_convite'],
                emails_informacoes['email_envio'],
                emails_informacoes['id_viagem']
               
            )
        )
        
        self.__conexao.commit()
        
    def enviar_emails_por_viagem(self, id_viagem: str) -> List[Tuple]:
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                SELECT * FROM TB_ENVIO_CONVITE WHERE id_viagem = ?
            ''', 
            (id_viagem,)
        )
        
        #fetchall só pega todos os emails cadastrados para uma viagem no banco
        viagem = cursor.fetchall()
        
        return viagem
    