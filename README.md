# Horóscopo

## Introdução
Aplicação Web que, a partir de uma data de nascimento fornecida pelo usuário, exibe o horóscopo correspondente ao signo. Texto do horóscopo é obtido através de uma requisição ao http://estilo.uol.com.br/horoscopo/leao/horoscopo-do-dia/.

## Installação
A API foi desenvolvida utilizando **Python3.4** com o Framework Flask. As bibliotecas necessárias se encontram no arquivo **api/requirements.txt**. Configuração do IP e Porta para rodar a API se encontra no arquivo **api/run.py**. Para simular um servidor, basta executar **node server.js** dentro da pasta **site/**, caso tenha o Node.js instalado. Para mudar a configuração do IP, basta ir no arquivo **site/app/app.module.js**.