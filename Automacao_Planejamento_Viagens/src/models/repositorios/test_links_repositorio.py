from typing import List, Tuple
from .links_repositorio import LinksRepositorio
from src.models.configuracoes.gerenciar_conexao_dba import gerenciar_conexao_dba
import pytest
import uuid

gerenciar_conexao_dba.conectar_banco_dados()
id_viagem = str(uuid.uuid4())
id_link = str(uuid.uuid4())

@pytest.mark.skip(reason="Testes com o banco de dados para registrar links")
def test_registrar_links():
    conexao = gerenciar_conexao_dba.get_conexao()
    links_repositorio = LinksRepositorio(conexao)
    
    links_informacoes = {
        "id_link": id_link,
        "id_viagem": id_viagem,
        "link": "https://github.com/KaiqueVfreitas",
        "titulo_email_viagem": "GitHub do desenvolvedor do"
    }
    
    links_repositorio.registrar_links(links_informacoes)
    
    conexao.commit()

@pytest.mark.skip(reason="Testes com o banco de dados para enviar links")
def test_envio_links_viagem() -> List[Tuple]: 
    conexao = gerenciar_conexao_dba.get_conexao()
    link_repositorio = LinksRepositorio(conexao)
    
    envio = link_repositorio.enviar_links_viagem(id_viagem)
   
    assert isinstance(envio, list)
    assert isinstance(envio[0], tuple)