
# Importação e persistência de preços de ativos - (iterate eureka)

## Objetivo

O objetivo desse projeto é criar uma ferramenta em Python para
importação diária de preços de ações utilizando a API Alpha Vantage
Inc. e persistência de dados com SQLite.

---

## Configurações Iniciais

 1. Tenha certeza de ter o [Python](https://www.python.org/downloads/) Instalado

 2. Crie um [ambiente virtual](https://docs.python.org/3/library/venv.html)

 3. Ative o novo ambiente virtual usando:

> source "name_used_to_create_venv"/bin/activate

 4. Instale dentro do novo ambiente virtual criado os pacotes nescessários executando no terminal:

> pip3 install -r requirements.txt

---

## Configurações da ferramenta

*Em todos os passos a seguir, sempre que for solicitado algum comando no terminal, e nescessário a ativação do ambiente virtual configurado acima.*

Primeiramente precisaremos criar o banco aonde os dados das requisições serão guardados (caso queira atrelar a ferramenta a um arquivo DB já existente vide próximo passo). 

Pra isso foi criado o arquivo **create_db.py** que já está configurado para criar o arquivo "*sqlite.db*".  Para executa-lo basta utilizar o terminal digitando:

> python3 create_db.py

Uma mensagem de status irá ser mostrada, avisando em caso positivo a criação do arquivo.

Dentro do projeto existe um arquivo chamado **amb_var.py**, ele tras possibilidade para acrescentar novos symbolos para serem cadastrados e alteração do nome do banco de dados, caso já exista um banco que queira atrelar a ferramenta. Precisaremos utilizar ele para adicionar a chave da API. Vá ao sita da API e faça o registro de sua chave ([Clique Aqui!](https://www.alphavantage.co/support/#api-key)) e adicione a chave dentro do co campo *KEY =* (lembrando de utilizar aspas simples para delimita-la)

Após esses procedimentos estamos prontos para utilizar a ferramenta


---

## Uso

A ferramenta roda unicamente com um comando:

> python3 main.py

Inicialmente, sem nenhum registro no banco a ferramenta irá iniciar o cadastro de todos os registros dos ultimos 7 dias (iniciando no dia 7 e finalizando no dia de "ontem")

A ferramenta sempre pegará os dados dos ultimos 7 dias, mas somente cadastrará as informações não registrados, previnindo registros duplicados. Caso os valores resgatados da API já estejam cadastrados no banco, a ferramenta os utilizará para atualizar os registros para ajuste de possíveis divergências de informações da própria "API Alpha Vantage Inc".

Todas as transações do db dentro da ferramenta geram mensagems de status no terminal, podendo ser mensagens de Erro de alguma falha no cadastro do banco ou mensagens de de status positivos apontando se foi criado um novo registro ou atualizado.
