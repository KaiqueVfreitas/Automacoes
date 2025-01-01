# Importações necessárias
import customtkinter as ctk
from .Menu import Menu
from controllers import LinkedinController  # Certifique-se de que o controlador está implementado corretamente
from tkinter import messagebox  # Para exibir mensagens ao usuário

class Index:
    def __init__(self):
        """Inicializa os componentes da tela e o controlador do LinkedIn."""
        self.linkedin_controller = LinkedinController()  # Instancia o controlador
        self.config_tela()
        self.ttl_pag()
        self.campo_email()
        self.campo_senha()
        self.btn_entrar()
        self.separador()
        self.btn_sair()
        self.janela.mainloop()

    # Métodos funcionalidades
    def receber_email_e_senha(self):
        """Captura email e senha, tenta login e decide se deve chamar a tela de menu."""
        email = self.txt_email.get()
        senha = self.txt_senha.get()

        # Tenta realizar o login no LinkedIn
        try:
            sucesso = self.linkedin_controller.linkedin(email, senha)
            if sucesso:  # Somente navega para o menu se o login for bem-sucedido
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                self.chamar_tela_menu()
            else:
                messagebox.showerror("Erro", "Login ou senha incorretos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def chamar_tela_menu(self):
        """Fecha a janela atual e abre a tela de menu."""
        self.janela.destroy()
        Menu()

    # Métodos visuais
    def config_tela(self):
        """Configura a aparência e as propriedades básicas da janela."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.janela = ctk.CTk()
        self.janela.geometry("350x550")
        self.janela.title("LinkedIn - Login")

    def ttl_pag(self):
        """Cria e posiciona o título da página."""
        ttl_pag = ctk.CTkLabel(
            self.janela,
            text="LOGIN NO LINKEDIN",
            font=("Helvetica", 20, "bold"),
            text_color="#F9F9F9",
        )
        ttl_pag.pack(pady=(30, 20))

    def campo_email(self):
        """Cria e posiciona o campo de entrada de e-mail."""
        self.txt_email = ctk.CTkEntry(
            self.janela,
            placeholder_text="Email",
            width=300,
            fg_color="#1A1A1A",
            text_color="#F3F3F3",
            placeholder_text_color="#A9A9A9",
        )
        self.txt_email.pack(pady=10)

    def campo_senha(self):
        """Cria e posiciona o campo de entrada de senha."""
        self.txt_senha = ctk.CTkEntry(
            self.janela,
            placeholder_text="Senha",
            show="*",
            width=300,
            fg_color="#1A1A1A",
            text_color="#F3F3F3",
            placeholder_text_color="#A9A9A9",
        )
        self.txt_senha.pack(pady=10)

    def btn_entrar(self):
        """Cria e posiciona o botão de login."""
        self.btn_login = ctk.CTkButton(
            self.janela,
            text="ENTRAR",
            command=self.receber_email_e_senha,  # Agora chama apenas o método de login
            width=300,
            corner_radius=8,
            font=("Helvetica", 14, "bold"),
            fg_color="#0077B5",
            hover_color="#005582",
        )
        self.btn_login.pack(pady=(20, 10))

    def btn_sair(self):
        """Cria e posiciona o botão de sair."""
        self.btn_sair = ctk.CTkButton(
            self.janela,
            text="SAIR",
            command=self.janela.destroy,  # Fecha a janela ao clicar no botão
            fg_color="#FF4B4B",
            hover_color="#D43F3F",
            width=100,
            corner_radius=8,
        )
        self.btn_sair.pack(pady=10)

    def separador(self):
        """Adiciona um separador visual."""
        separator = ctk.CTkLabel(
            self.janela,
            text="\u2500" * 20 + " ou " + "\u2500" * 20,
            font=("Helvetica", 12),
            text_color="#A9A9A9",
        )
        separator.pack(pady=15)
