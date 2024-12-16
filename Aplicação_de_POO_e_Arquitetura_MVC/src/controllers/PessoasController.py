import sys
from models.Pessoas import Pessoas
from typing import List
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

class PessoasController:
    pessoa = []
    @classmethod
    def metodo_salvar_pessoas(cls, Pessoas: Pessoas) -> None:
        cls.pessoa.append(Pessoas)

    @classmethod
    def metodo_listar_pessoas(cls) -> List[Pessoas]:
        return cls.pessoa