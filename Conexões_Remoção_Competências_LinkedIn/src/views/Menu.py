import customtkinter as ctk

class Menu():
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        janela = ctk.CTk()
        janela.geometry("350x500")
        janela.title("LinkedIn - Menu")
        
        ttl_pag = ctk.CTkLabel(
            janela,
            text="MENU",
            font=("Helvetica", 20, "bold"),
            text_color="#F9F9F9",
        )
        ttl_pag.pack(pady=(30, 20))
        
        btn_conectar = ctk.CTkButton(
            janela,
            text="Conectar com novas pessoas",
            width=300,
            height=90,
            corner_radius=8,
            font=("Helvetica", 14, "bold"),
            fg_color="#28A745",
            hover_color="#218838",
        )
        btn_conectar.pack(pady=10)
        
        btn_remover_competencias = ctk.CTkButton(
            janela,
            text="Remover Competências",
            width=300,
            height= 90,
            corner_radius=8,
            font=("Helvetica", 14, "bold"),
            fg_color="#DC3545",
            hover_color="#C82333",
        )
        btn_remover_competencias.pack(pady=10)
        
        janela.mainloop()
        
        def acao_conectar(self):
            pass
        def metodo_remover_competencias(self):
            pass
      
        
        