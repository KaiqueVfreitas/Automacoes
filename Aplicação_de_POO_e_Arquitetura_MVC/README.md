<h1>📚 Aplicação de POO e Arquitetura MVC</h1>
<p>
  Este projeto foi desenvolvido com o objetivo de demonstrar a aplicação de Programação Orientada a Objetos (POO) e a organização de código utilizando a Arquitetura MVC (Model-View-Controller). 
</p>
<p>
  <b>Observação:</b> Este projeto tem fins exclusivamente didáticos e todos os comentários e decisões implementadas foram feitos para facilitar o aprendizado e a demonstração técnica.
</p>

<h2>🎯 Objetivo do Projeto</h2>
<ul>
  <li>Implementar uma estrutura organizada com base na Arquitetura MVC.</li>
  <li>Aplicar conceitos fundamentais de Programação Orientada a Objetos, como classes, encapsulamento e responsabilidades separadas.</li>
  <li>Desenvolver um sistema simples capaz de cadastrar informações de pessoas (nome, sobrenome, idade e CPF).</li>
</ul>

<h2>🗂️ Estrutura do Projeto</h2>
<p>
  O projeto foi organizado seguindo a arquitetura MVC, com diretórios separados para <b>models</b>, <b>controllers</b>, e <b>views</b>. Além disso, os testes estão localizados em uma pasta específica.
</p>

<pre>
📁 Aplicacao_POO_MVC/
│
├── venv/                # Ambiente virtual Python
├── doc/                 # Documentação
│   └── explicacao.mk    # Arquivos de explicação ou documentação adicional
│
├── src/                 # Código-fonte principal
│   ├── controllers/
│   │   └── PessoasController.py  # Lógica de controle do sistema
│   │
│   ├── models/
│   │   └── Pessoas.py            # Definição do modelo Pessoa
│   │
│   └── views/
│       └── index.py              # Interface simples de interação
│
├── test/                # Testes automatizados
│   └── test_models.py   # Testes do modelo usando Pytest
│
└── README.md            # Documentação principal
</pre>

<h2>🛠️ Tecnologias e Convenções</h2>
<ul>
  <li><b>Python 3:</b> Linguagem de programação principal.</li>
  <li><b>Arquitetura MVC:</b> Separação do código em Model, View e Controller.</li>
  <li><b>POO:</b> Aplicação de classes e princípios de encapsulamento.</li>
  <li><b>Pytest:</b> Biblioteca utilizada para os testes automatizados.</li>
</ul>

<h2>🚀 Funcionamento do Projeto</h2>
<p>
  O projeto é um sistema simples para cadastro de pessoas com as seguintes informações:
</p>
<ul>
  <li>Nome</li>
  <li>Sobrenome</li>
  <li>Idade</li>
  <li>CPF</li>
</ul>
<p>
  A responsabilidade de cada parte do projeto está definida conforme a Arquitetura MVC:
</p>

<h3>📌 Models</h3>
<ul>
  <li><b>Pessoas.py:</b> Classe responsável por armazenar os dados das pessoas (nome, sobrenome, idade, CPF).</li>
</ul>

<h3>📌 Controllers</h3>
<ul>
  <li><b>PessoasController.py:</b> Controlador que gerencia as operações relacionadas ao modelo, como salvar ou manipular os dados.</li>
</ul>

<h3>📌 Views</h3>
<ul>
  <li><b>index.py:</b> Interface simples de interação que permite ao usuário inserir dados e visualizar os resultados.</li>
</ul>

<h2>🧪 Testes</h2>
<p>
  O projeto utiliza a biblioteca <b>pytest</b> para realizar testes automatizados. Todos os testes estão localizados no arquivo <b>test/test_models.py</b>.  
</p>
<p>
  <b>Observação:</b> Apesar de utilizar o padrão <i>PascalCase</i> para as classes, o arquivo de teste segue a convenção <i>snake_case</i>. Isso ocorre devido às normas do <b>pytest</b>, que exige que os nomes das funções e arquivos de teste sigam o padrão <i>snake_case</i> para serem reconhecidos automaticamente.
</p>

<h2>🔠 Convenções de Nomeação</h2>
<p>
  As convenções de nomeação adotadas seguem as normas padrão do Python:
</p>
<ul>
  <li><b>PascalCase:</b> Utilizado exclusivamente para nomes de classes (exemplo: <code>Pessoas</code>).</li>
  <li><b>snake_case:</b> Utilizado para nomes de arquivos, funções e variáveis (exemplo: <code>pessoas_controller.py</code>).</li>
</ul>
<p>
  <b>Exceção:</b> No diretório <code>test/</code>, o padrão <i>snake_case</i> foi adotado para nomear os arquivos devido à necessidade de compatibilidade com a biblioteca <b>pytest</b>.
</p>

<h2>🧩 Exemplos de Uso</h2>
<p>Para executar o projeto, siga os passos abaixo:</p>

<ol>
  <li>Clone este repositório:
    <pre>
git clone https://github.com/seu-usuario/Aplicacao_POO_MVC.git
    </pre>
  </li>
  <li>Ative o ambiente virtual:
    <pre>
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
    </pre>
  </li>
  <li>Instale as dependências necessárias:
    <pre>
pip install -r requirements.txt
    </pre>
  </li>
  <li>Execute a view principal:
    <pre>
python src/views/index.py
    </pre>
  </li>
</ol>

<h2>🎓 Comentários Didáticos</h2>
<p>
  Este projeto foi estruturado para fins de aprendizado. A arquitetura e os comentários presentes no código foram cuidadosamente adicionados para facilitar a compreensão das decisões técnicas e das boas práticas de programação.
</p>
<p>
  Se você está estudando POO ou Arquitetura MVC, este projeto pode servir como um guia prático e uma base para expandir funcionalidades.
</p>

<h2>📬 Contato</h2>
<p>
  Se tiver dúvidas, sugestões ou quiser conhecer mais sobre meu trabalho <a href="https://kaiquevfreitas.github.io/Site_Portifolio/">CLIQUE AQUI</a>
</p>
