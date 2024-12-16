import sys
sys.path.append(".")
from src.models import Pessoas

def test_concatenacao_nome_sobrenome():
    p1 = Pessoas.Pessoas("Joao", "Silva", 20, "123.456.789-00")
    assert p1.nome_completo() == "Joao Silva"
    