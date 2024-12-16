# 📘 Documentação do Projeto

Este documento apresenta uma visão geral do projeto, explicando sua arquitetura, funcionamento, bibliotecas utilizadas, e instruções de uso. O objetivo é fornecer uma base clara e detalhada para entender como o sistema foi desenvolvido e como ele deve ser utilizado.

---

## 🗂️ Estrutura do Projeto

O projeto está organizado em três diretórios principais, cada um com uma função específica:

### 1. **`doc/`**
- **Descrição:** Diretório destinado a toda a documentação do projeto.
- **Conteúdo:** 
  - Diagramas de casos de uso.
  - Modelos conceituais de banco de dados.
  - Manuais de instrução e guias de uso do sistema.
  - Explicações sobre o funcionamento do código.
- **Objetivo:** Centralizar as informações que apoiam o entendimento e a manutenção do projeto.

### 2. **`src/`**
- **Descrição:** Diretório que contém todo o código-fonte do sistema.
- **Conteúdo:**
  - **`controllers/`**: Gerencia a transição entre a camada de dados (Model) e a interface de usuário (View).
  - **`models/`**: Responsável pelo gerenciamento do banco de dados e modelagem das informações.
  - **`views/`**: Gerencia as interações com o usuário, exibindo informações e capturando entradas.
- **Objetivo:** Centralizar toda a lógica do sistema, com uma estrutura modular baseada na Arquitetura MVC.

### 3. **`test/`**
- **Descrição:** Diretório usado para desenvolvimento orientado a testes (TDD).
- **Conteúdo:**
  - Cópias controladas das funções do projeto para validar alterações e melhorias.
  - Testes automatizados utilizando a biblioteca Pytest.
- **Objetivo:** Garantir a qualidade do código e a estabilidade do sistema ao implementar novas funcionalidades ou corrigir bugs.

---

## 🏗️ Arquitetura do Projeto

O projeto foi desenvolvido seguindo a **Arquitetura MVC (Model-View-Controller)**, uma abordagem amplamente utilizada para garantir organização, escalabilidade e separação de responsabilidades. 

### Papéis de Cada Camada:
1. **Model**:
   - Gerencia o acesso e manipulação dos dados no banco de dados.
   - Modelagem de dados para cadastro de pessoas (nome, sobrenome, idade, CPF).
   
2. **Controller**:
   - Atua como intermediário entre o Model e a View.
   - Controla a lógica do sistema e oferece métodos para listar e salvar pessoas no banco de dados.

3. **View**:
   - Gerencia a interação com o usuário.
   - Inclui um loop principal que chama os métodos das camadas Controller e Model, exibindo informações e recebendo entradas.

Essa arquitetura foi escolhida para:
- Separar responsabilidades, tornando o código mais organizado e fácil de manter.
- Facilitar a reutilização de componentes e a expansão do sistema.
- Seguir boas práticas amplamente adotadas em projetos de software.

---

## 🔧 Bibliotecas Utilizadas

O projeto faz uso das seguintes bibliotecas:
- **Python 3:** Linguagem principal para o desenvolvimento.
- **Pytest:** Biblioteca para realização de testes automatizados. Foi utilizada para garantir o correto funcionamento das funções, como a concatenação de nome e sobrenome.
  
Para instalar as dependências necessárias, utilize o comando:
```bash
pip install -r requirements.txt
