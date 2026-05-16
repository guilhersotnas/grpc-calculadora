Pode copiar e colar exatamente isso no `README.md` do GitHub:

````md
# Calculadora Distribuída com gRPC

Projeto desenvolvido utilizando Python e gRPC para implementação de uma calculadora distribuída com operações matemáticas básicas, avançadas e comunicação por streaming.

## Integrantes

- Bianca Nicolli Celso dos Santos
- Gabriella Silvestre Annunciato
- Giovanna Silvestre Annunciato
- Guilherme dos Santos Ferreira

FATEC Antonio Russo – São Caetano do Sul  
AMS ADS 2º Semestre

---

# Tecnologias Utilizadas

- Python 3
- gRPC
- Protocol Buffers (protobuf)
- grpcio
- grpcio-tools

---

# Estrutura do Projeto

```bash
.
├── cliente.py
├── servidor.py
├── exemplo.proto
├── exemplo_pb2.py
├── exemplo_pb2_grpc.py
├── README.md
└── venv/
````

---

# Funcionalidades

## Operações Unary

* Somar
* Subtrair
* Multiplicar
* Dividir
* Potência
* Raiz Quadrada

## Streaming

### Client Streaming

* Soma de vários números enviados pelo cliente

### Server Streaming

* Geração de tabuada do número informado

### Bidirectional Streaming

* Cálculo de média móvel em tempo real

---

# Como Executar o Projeto

## 1 - Clonar o repositório

```bash
git clone https://github.com/guilhersotnas/grpc-calculadora.git
```

---

## 2 - Entrar na pasta do projeto

```bash
cd grpc-calculadora
```

---

## 3 - Criar ambiente virtual

```bash
python3 -m venv venv
```

---

## 4 - Ativar ambiente virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5 - Instalar dependências

```bash
pip install grpcio grpcio-tools
```

---

## 6 - Gerar arquivos do protobuf

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. exemplo.proto
```

---

## 7 - Executar o servidor

```bash
python servidor.py
```

---

## 8 - Executar o cliente

Abra outro terminal e execute:

```bash
python cliente.py
```

---

# Exemplo de Uso

## Menu Interativo

```bash
===== CALCULADORA gRPC =====
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Potência
6 - Raiz Quadrada
7 - Somar Stream
8 - Gerar Tabuada
9 - Média Móvel
0 - Sair
```

---

# Tratamento de Erros

O sistema possui:

* Tratamento para divisão por zero
* Validação de entrada de dados
* Tratamento de erro de conexão com servidor
* Comunicação remota utilizando gRPC

---

# Objetivo do Projeto

Desenvolver um sistema distribuído utilizando gRPC para comunicação entre cliente e servidor, explorando os diferentes tipos de RPC:

* Unary
* Client Streaming
* Server Streaming
* Bidirectional Streaming

---

# Autor

Projeto acadêmico desenvolvido para a disciplina de Microsserviços e Sistemas Distribuídos.
