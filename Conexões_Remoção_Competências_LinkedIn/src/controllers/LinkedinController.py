# Importações necessárias para controlar o navegador e exibir mensagens ao usuário
from tkinter import messagebox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LinkedinController:
    def __init__(self):
        """Inicializa as variáveis do navegador e serviço."""
        self.navegador = None
        self.servico = None

    def iniciar_chrome_drive(self):
        """Inicializa o serviço do ChromeDriver."""
        self.servico = Service(ChromeDriverManager().install())

    def configuracoes_navegador(self):
        """Define configurações específicas do navegador.
        - Modo anônimo.
        - Desabilitar extensões.
        - Janela com tamanho específico.
        """
        chrome_opcoes = Options()
        chrome_opcoes.add_argument("--disable-extensions")
        chrome_opcoes.add_argument("--incognito")
        chrome_opcoes.add_argument("--window-size=650,350")
        return chrome_opcoes

    def executar_navegador(self):
        """Executa o navegador com as configurações especificadas.
        Lança uma exceção caso o serviço do ChromeDriver não esteja inicializado.
        """
        if not self.servico:
            raise Exception("Serviço do navegador não iniciado.")
        chrome_opcoes = self.configuracoes_navegador()
        self.navegador = webdriver.Chrome(service=self.servico, options=chrome_opcoes)

    def abrir_linkedin(self, url: str = "https://www.linkedin.com/login"):
        """Abre a página de login do LinkedIn.
        - Lança uma exceção se o navegador não estiver inicializado.
        """
        if not self.navegador:
            raise Exception("Navegador não iniciado.")
        self.navegador.get(url)

    def esperar_elemento(self, by: By, value: str, timeout: int = 10):
        """Espera um elemento específico carregar na página dentro de um tempo limite."""
        return WebDriverWait(self.navegador, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def preencher_campo(self, by: By, value: str, texto: str):
        """Localiza um campo no formulário e insere o texto informado."""
        campo = self.esperar_elemento(by, value)
        campo.clear()
        campo.send_keys(texto)

    def clicar_botao(self, by: By, value: str):
        """Localiza e clica em um botão."""
        botao = self.esperar_elemento(by, value)
        botao.click()

    def login_linkedin(self, email: str, senha: str):
        """Executa o processo de login no LinkedIn.
        - Preenche os campos de e-mail e senha.
        - Clica no botão de login.
        """
        self.preencher_campo(By.ID, "username", email)
        self.preencher_campo(By.ID, "password", senha)
        self.clicar_botao(By.XPATH, "//button[@type='submit']")

    def verificar_login(self):
        """Verifica se o login foi realizado com sucesso.
        - Retorna True se o perfil do usuário carregar.
        - Retorna False caso contrário.
        """
        try:
            self.esperar_elemento(By.CLASS_NAME, "profile-card-name", 10)
            return True
        except Exception:
            return False

    def fechar_navegador(self):
        """Fecha o navegador caso ele esteja aberto."""
        if self.navegador:
            self.navegador.quit()

    def linkedin(self, email: str, senha: str):
        """Fluxo completo de login no LinkedIn:
        - Inicia o navegador.
        - Abre o LinkedIn.
        - Realiza o login.
        - Verifica se o login foi bem-sucedido.
        - Exibe mensagens ao usuário e fecha o navegador.
        """
        try:
            self.iniciar_chrome_drive()
            self.executar_navegador()
            self.abrir_linkedin()
            self.login_linkedin(email, senha)

            if self.verificar_login():
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha no login. Verifique suas credenciais.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        finally:
            self.fechar_navegador()
