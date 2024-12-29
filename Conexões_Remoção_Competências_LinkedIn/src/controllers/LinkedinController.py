from typing import List
from models import Linkedin

class LinkedinController:
      @classmethod
      def clique(cls) -> None:
        print("Botão clicado!")
        
      @classmethod
      def metodo_login_linkedin(cls, email: str, senha: str) -> None:
        
        if not email or not senha:
            print("Todos os campos devem ser preenchidos.")
        else:
            print(f"Email: {email}")
            print(f"Senha: {senha}")
            print("Não são armazenados, apenas usados na automação")