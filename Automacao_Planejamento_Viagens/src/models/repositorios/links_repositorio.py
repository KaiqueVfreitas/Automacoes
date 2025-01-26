
from sqlite3 import Connection
from typing import Dict, List, Tuple



class LinksRepositorio:
    def __init__(self, conexao: Connection) -> None:
        self.__conexao = conexao
        
    def registrar_links(self, links_informacoes: Dict) -> None: 
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                INSERT INTO TB_LINKS (
                    id_link, id_viagem, titulo_email_viagem, link
                ) VALUES (
                    ?, ?, ?, ?
                )
            ''', 
            (
                links_informacoes['id_link'],
                links_informacoes['id_viagem'],
                links_informacoes['titulo_email_viagem'],
                links_informacoes['link'],
               
            )
        )
        
        self.__conexao.commit()
        
    def enviar_links_viagem(self, id_viagem: str) -> List[Tuple]:
        cursor = self.__conexao.cursor()
        
        cursor.execute(
            '''
                SELECT * FROM TB_LINKS WHERE id_viagem = ?
            ''', 
            (id_viagem,)
        )
        
        #fetchall só pega todos os emails cadastrados para uma viagem no banco
        links = cursor.fetchall()
        
        return links

