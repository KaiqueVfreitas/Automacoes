from typing import List, Tuple
import pytest
import uuid
from src.models.configuracoes.gerenciar_conexao_dba import gerenciar_conexao_dba
from .enviar_emails_convite_viagem_repository import EnviarEmailsConviteViagemRepository

gerenciar_conexao_dba.conectar_banco_dados()
id_viagem = str(uuid.uuid4())

def test_registrar_emails_participantes():
    conexao = gerenciar_conexao_dba.get_conexao()
    enviar_emails_convite_repository = EnviarEmailsConviteViagemRepository(conexao)
    
    emails_informacoes_viagem = {
        "id_envio_convite": str(uuid.uuid4()),
        "id_viagem": id_viagem,
        "email_envio": "teste@teste.com"
    }
    
    enviar_emails_convite_repository.registrar_emails_participantes(emails_informacoes_viagem)
    
    conexao.commit()
    
def test_enviar_emails_por_viagem():
    conexao = gerenciar_conexao_dba.get_conexao()
    enviar_emails_convite_repository = EnviarEmailsConviteViagemRepository(conexao)
    
    emails = enviar_emails_convite_repository.enviar_emails_por_viagem(id_viagem)
    