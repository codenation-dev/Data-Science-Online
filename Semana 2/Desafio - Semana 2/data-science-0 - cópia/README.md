# Pré-processamento de dados em Python

Neste desafio vamos praticar a manipulação de dados utilizando
a biblioteca [pandas](https://pandas.pydata.org/). Manipulação de dados é uma das tarefas
mais fundamentais para um cientista de dados e o pandas - biblioteca mais popular do Python no assunto - ajuda a tornar essa tarefa mais agradável.

## Objetivo

O objetivo deste desafio é extrair algumas informações quantitativas
que nos ajudem a compreender a natureza dos dados à disposição e ganhar alguns _insights_
sobre o _data set_.

Para isso, utilizaremos o _data set_ [Black Friday](https://codenation-challenges.s3-us-west-1.amazonaws.com/data-science-0/black_friday.csv)
disponibilizado originalmente pela [Analytics Vidhya](https://www.analyticsvidhya.com/) e acessível
publicamente através do [Kaggle](https://www.kaggle.com). O _data set_ traz algumas variáveis relativas à transações comerciais
realizadas durante a Black Friday em uma determinada loja de varejo. Cada observação é relativa
a um determinado item comprado por um usuário e um usuário pode ter comprado mais de um item.

## Tópicos

Neste desafios nós vamos explorar:

* Python
* Pandas
* Jupyter notebook

## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```
