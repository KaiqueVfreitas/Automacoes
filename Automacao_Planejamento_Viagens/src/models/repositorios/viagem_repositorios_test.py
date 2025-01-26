import uuid
import pytest
from datetime import datetime, timedelta
from .viagem_repositorios import ViagemRepositorios
from src.models.configuracoes.gerenciar_conexao_dba import gerenciar_conexao_dba

gerenciar_conexao_dba.conectar_banco_dados()
id_viagem = str(uuid.uuid4())

@pytest.mark.skip(reason="Testes com o banco de dados para criar viagem")
def test_criar_viagem():
    conexao = gerenciar_conexao_dba.get_conexao()
    viagem_repositorio = ViagemRepositorios(conexao)
    
    viagem_informacoes = {
        'id_viagem': id_viagem, 
        'destino_viagem': 'Palmas - Tocantins', 
        'data_inicio': datetime.strptime("19-09-2025", "%d-%m-%Y"), 
        'data_fim': datetime.strptime("19-09-2025", "%d-%m-%Y") + timedelta(days=10), 
        'nome_organizador': 'Ricardo Oliveira',
        'email_organizador': 'RicardoOliveira@teste.com'
    }
    
    viagem_repositorio.criar_viagem(viagem_informacoes)
    conexao.commit()

@pytest.mark.skip(reason="Testes com o banco de dados para encontrar viagem")
def test_encontrar_viagem_por_id():
    conexao = gerenciar_conexao_dba.get_conexao()
    viagem_repositorio = ViagemRepositorios(conexao)
    
    viagem_encontrada = viagem_repositorio.encontrar_viagem_por_id(id_viagem)
    print(viagem_encontrada)

@pytest.mark.skip(reason="Testes com o banco de dados para alterar status viagem")
def test_mudar_status_viagem():
    conexao = gerenciar_conexao_dba.get_conexao()
    viagem_repositorio = ViagemRepositorios(conexao)
    
    viagem = viagem_repositorio.mudar_status_viagem(id_viagem)
    