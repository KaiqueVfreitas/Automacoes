from ..models import Pessoas
from typing import List
class PessoaController:
    pessoa = []
    
    @classmethod
    def salvar_pessoa(cls, Pessoas: Pessoas) -> None:
        cls.pessoa.append(Pessoas)

    @classmethod
    def listar_pessoa(cls) -> List[Pessoas]:
        return cls.pessoa