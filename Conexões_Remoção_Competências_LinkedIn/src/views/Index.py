import customtkinter as ctk
from controllers import LinkedinController

class Index:
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")

    janela = ctk.CTk()
    janela.geometry("350x500")
    janela.title("LinkedIn - Login")

    # Título principal
    ttl_pag = ctk.CTkLabel(
         janela, 
         text="LOGIN NO LINKEDIN", 
         font=("Helvetica", 20, "bold"), 
         text_color="#F9F9F9"
     )
    ttl_pag.pack(
         pady=(30, 20)
     )

    
    txt_email = ctk.CTkEntry(
         janela, 
         placeholder_text="Email", 
         width=300, 
         fg_color="#1A1A1A", 
         text_color="#F3F3F3", 
         placeholder_text_color="#A9A9A9"
     )
    txt_email.pack(
         pady=10
     )


    txt_senha = ctk.CTkEntry(
         janela, 
         placeholder_text="Senha", 
         show="*", 
         width=300, 
         fg_color="#1A1A1A", 
         text_color="#FFFFFF", 
         placeholder_text_color="#A9A9A9"
     )
    txt_senha.pack(
         pady=10
     )

     
    btn_login = ctk.CTkButton(
         janela, 
         text="ENTRAR", 
         command=LinkedinController.clique, 
         width=300, 
         corner_radius=8, 
         font=("Helvetica", 14, "bold"), 
         fg_color="#0077B5", 
         hover_color="#005582"
     )
    btn_login.pack(
         pady=(20, 10)
    )

    
    btn_cad = ctk.CTkButton(
         janela, 
         text="NOVO USUÁRIO", 
         command=LinkedinController.clique, 
         fg_color="transparent", 
         text_color="#0077B5", 
         hover_color="#005582", 
         font=("Helvetica", 13, "bold")
)
    btn_cad.pack(
         pady=5
     )

    
    separator = ctk.CTkLabel(
         janela, 
         text="\u2500" * 20 + " ou " + "\u2500" * 20, 
         font=("Helvetica", 12), 
         text_color="#A9A9A9"
     )
    separator.pack(
         pady=15
     )

    
    btn_sair = ctk.CTkButton(
         janela, 
         text="SAIR", 
         command=LinkedinController.clique, 
         fg_color="#FF4B4B", 
         hover_color="#D43F3F", 
         width=100, 
         corner_radius=8
     )
    
    btn_sair.pack(
         pady=10
     )


    janela.mainloop()
