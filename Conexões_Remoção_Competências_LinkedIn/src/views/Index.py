#Afim de facilitar a manutenção do codigo criei muitos métodos. Organizei em três tipos de metodos: Metodos funcionalidades (passa o login e senha do linkendin para a controller e chama a tela menu), Metodos visuais (componentes da tela) e Metodos de junção de componentes(tela montada)
import customtkinter as ctk
from .Menu import Menu
from controllers import LinkedinController

class Index:
    #Métodos funcionalidades
    def receber_email_e_senha(self):
        email = self.txt_email.get()
        senha = self.txt_senha.get()
        LinkedinController.metodo_acessar_linkedin(email, senha)
        
    def chamar_tela_menu(self):
        self.janela.destroy()
        tela_menu = ctk.CTk()
        menu = Menu(tela_menu)
        menu.pack(fill="both", expand=True)
        menu.mainloop()
        return
        
    def juntar_metodos(self):
        self.chamar_tela_menu()
        self.receber_email_e_senha()
    #Métodos visuais 
    def config_tela(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.janela = ctk.CTk()
        self.janela.geometry("350x500")
        self.janela.title("LinkedIn - Login")

    def ttl_pag(self):
        ttl_pag = ctk.CTkLabel(
            self.janela,
            text="LOGIN NO LINKEDIN",
            font=("Helvetica", 20, "bold"),
            text_color="#F9F9F9",
        )
        ttl_pag.pack(pady=(30, 20))

    def campo_email(self):
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
        self.btn_login = ctk.CTkButton(
            self.janela,
            text="ENTRAR",
            command=self.juntar_metodos,
            width=300,
            corner_radius=8,
            font=("Helvetica", 14, "bold"),
            fg_color="#0077B5",
            hover_color="#005582",
        )
        self.btn_login.pack(pady=(20, 10))
        

    def btn_sair(self):
        self.btn_sair = ctk.CTkButton(
            self.janela,
            text="SAIR",
            command=self.janela.destroy,
            fg_color="#FF4B4B",
            hover_color="#D43F3F",
            width=100,
            corner_radius=8,
        )
        self.btn_sair.pack(pady=10)

    def separador(self):
        separator = ctk.CTkLabel(
            self.janela,
            text="\u2500" * 20 + " ou " + "\u2500" * 20,
            font=("Helvetica", 12),
            text_color="#A9A9A9",
        )
        separator.pack(pady=15)


    #Junção dos componentes visuais
    def __init__(self):
        self.config_tela()
        self.ttl_pag()
        self.campo_email()
        self.campo_senha()
        self.btn_entrar()
        self.separador()
        self.btn_sair()
        self.janela.mainloop()
   
