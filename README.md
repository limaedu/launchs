<h1 align = 'center'>  Launchs API</h1>
<h2 align = 'center'>
<a href="https://docs.spacexdata.com/#bc65ba60-decf-4289-bb04-4ca9df01b9c1">Documentation</a>
</h2>

---
### 1. 📁  <u>**Clonando o projeto</u>**

```cmd
$ git clone https://github.com/limaedu/launchs
```
#### **1.1 (Opcional) Criando um ambiente virtual**
```cmd
$ pip install virtualenv
```
```cmd
$ virtualenv -p python3 <nome_do_ambiente> #criando ambiente
$ .\<nome_do_ambiente>\scripts\activate #ativando

```

#### **1.2 Instalando dependências**
```cmd
$ pip install requests
$ pip install xlsxwriter
$ pip install unittest 
```
Alternativamente, é possível instalar através do arquivo requirements.txt utilizando o comando
```cmd
$ pip install -r requirements.txt
```


---

### **2.  <u>Respondendo os itens solicitados</u>**
Para executar o script que responde os itens basta executar o comando

```cmd
$ py desafio.py
```

---

### **3.  <u>Testes</u>**
Foi utilizada a biblioteca [unittest](https://docs.python.org/3/library/unittest.html) para a realização dos testes, tanto para a parte com Mock, quanto a parte sem Mock. O padrão utilizado para os testes foi o [Arrange-Act-Assert](http://wiki.c2.com/?ArrangeActAssert) com inspiração na metologia [TDD](http://agiledata.org/essays/tdd.html).
#### **3.1 Testes sem Mock**
Foram realizados 4 testes unitários para a API:

- Teste básico de requisição: validar se recebemos uma resposta com status code 200
- Teste de requisição sem parâmetros: validar se recebemos uma lista vazia caso sejam enviados parâmetros inválidos
- Teste de validação lançamentos no ano de 2020: validar se o número de voos encontrados no ano de 2020 (ano com mais voos) bate com o encontrado no script desafio.py
- Teste de validação lançamentos no Cabo Canaveral: validar se o número de voos encontrados em Cabo Canaveral (local com mais voos) bate com o encontrado no script desafio.py

A Classe de teste se encontra no arquivo test_launch_gateway.py e a Classe com os métodos se encontra no arquivo launch_gateway.py.

Para executar os testes, basta executar os comandos

```cmd
$ cd test/no_mock
$ py -m unittest test_launch_gateway.py

```
#### **3.2 Testes com Mock**
Pensando em casos reais onde temos API's mais complexas e muito mais testes, foi utilizado o Mock para simularmos as requisições.

Foram realizados 2 testes com Mock:

- Teste básico de requisição: validar se recebemos uma resposta com status code 200
- Teste do json de resposta com flight_number: validar se recebemos uma resposta certa para o flight_number passado de acordo com o json sample que se encontra no arquivo sample_json.json

Para executar os testes, basta executar os comandos

```cmd
$ cd test/mock
$ py -m unittest test_launch_gateway.py

```



