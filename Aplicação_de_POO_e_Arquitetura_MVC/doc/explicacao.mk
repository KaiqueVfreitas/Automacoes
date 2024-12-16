doc é a pasta que fica toda a documentação dos projetos como execmplo: diagramas de casos e uso, modelos conceituais de banco de dados, manual de instrução do sistema, como deve usar o sistema, etc...

src é a pasta de fato com todo o projeto usado para guardar o codigo fonte usado na pratica

teste é a pasta usada para desenvolvimento orientado a testes, uma copia do projeto para testar alterações e melhorias

dentro do tests e src, tem as pastas controllers, view e model cada um tem suas funções
    model fica responsavel pelo manuseio do banco
    view fica responsavel por todas as intereções do usuario
    controllers fica responsavel pela transição entre banco e view

    No caso da model atual, temos toda modelagem de dados, de um banco que tem inforamções de pessoas para cadastro
    Na controllers foram criados dois metodos um de listar e outro de salvar
    Na view tem um loop para rodar os metodos das controllers e model

Na pasta test, houve tambem uma demonstração de uso com o metodo test_concatenacao_nome_sobrenome, uso nele o assert que retorna sempre verdadeiro para ter certeza que a concatenação funcionol. Mas para todo o projeto funcionar tive que baixar o pytest