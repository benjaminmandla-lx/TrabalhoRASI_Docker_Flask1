# TrabalhoRASI_Docker_Flask1

# Docker com Aplicação Python/Flask

Projeto desenvolvido para a disciplina de **Redes e Administração de Sistemas (RASI)** do **Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) — Campus Campos do Jordão**.

---

## Objetivo

Este projeto tem como objetivo demonstrar a criação, configuração e execução de uma aplicação web desenvolvida em **Python utilizando o framework Flask**, executada dentro de um **contêiner Docker** em um ambiente **Ubuntu Server**.

A aplicação disponibiliza uma página inicial e duas páginas adicionais, acessíveis através de diferentes rotas.

---

## Tecnologias Utilizadas

* **Ubuntu Server** — sistema operacional utilizado no ambiente do servidor.
* **Docker** — plataforma utilizada para criação e execução do contêiner.
* **Python 3.14 Slim** — imagem base utilizada no contêiner.
* **Flask 3.1.2** — framework utilizado para desenvolvimento da aplicação web.

---

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

```text
projeto-flask/
├── Dockerfile
└── app/
    ├── app.py
    └── requirements.txt
```

### Descrição dos arquivos

| Arquivo                | Descrição                                                   |
| ---------------------- | ----------------------------------------------------------- |
| `Dockerfile`           | Define as instruções utilizadas para criar a imagem Docker. |
| `app/app.py`           | Contém o código da aplicação Flask e suas rotas.            |
| `app/requirements.txt` | Lista as dependências Python utilizadas pela aplicação.     |

---

## Aplicação Flask

O arquivo `app.py` contém uma aplicação Flask simples, disponibilizando três rotas:

| Rota       | Descrição                                                 |
| ---------- | --------------------------------------------------------- |
| `/`        | Página inicial da aplicação.                              |
| `/segredo` | Página temática sobre o segredo da empresa.               |
| `/membros` | Página contendo uma lista fictícia de membros da empresa. |

---

## Requirements

O arquivo `requirements.txt` contém a dependência necessária para executar a aplicação:

```txt
Flask==3.1.2
```

---

## Dockerfile

O `Dockerfile` utilizado no projeto é:

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Funcionamento do Dockerfile

* `FROM python:3.14-slim` — utiliza uma imagem compacta do Python 3.14 como base.
* `WORKDIR /app` — define `/app` como diretório de trabalho dentro do contêiner.
* `COPY app/requirements.txt .` — copia o arquivo de dependências para o contêiner.
* `RUN pip install...` — instala o Flask e as demais dependências.
* `COPY app/ .` — copia os arquivos da aplicação para o contêiner.
* `EXPOSE 5000` — informa que a aplicação utiliza a porta 5000.
* `CMD ["python", "app.py"]` — inicia a aplicação Flask quando o contêiner é executado.

---

# Execução do Projeto

## 1. Verificar o Docker

Antes de iniciar o projeto, verifique se o Docker está instalado e funcionando:

```bash
docker --version
```

Também é possível verificar o serviço:

```bash
sudo systemctl status docker
```

Caso seja necessário iniciar o Docker:

```bash
sudo systemctl start docker
```

---

## 2. Acessar o diretório do projeto

Entre no diretório onde estão os arquivos do projeto:

```bash
cd ~/projeto-flask
```

A estrutura pode ser conferida com:

```bash
find . -maxdepth 2 -type f
```

O resultado deverá apresentar arquivos semelhantes a:

```text
./Dockerfile
./app/app.py
./app/requirements.txt
```

---

## 3. Construir a imagem Docker

No diretório que contém o `Dockerfile`, execute:

```bash
sudo docker build -t minha-flask .
```

O comando cria uma imagem chamada:

```text
minha-flask
```

Para verificar se a imagem foi criada:

```bash
sudo docker images
```

---

## 4. Executar o contêiner

Após construir a imagem, execute:

```bash
sudo docker run -d -p 5000:5000 --name meu-flask minha-flask
```

### Explicação

* `-d` — executa o contêiner em segundo plano.
* `-p 5000:5000` — conecta a porta 5000 da máquina à porta 5000 do contêiner.
* `--name meu-flask` — define o nome do contêiner.
* `minha-flask` — nome da imagem utilizada.

---

## 5. Verificar o contêiner

Para verificar se o contêiner está em execução:

```bash
sudo docker ps
```

O resultado deverá apresentar o contêiner `meu-flask` com a porta:

```text
0.0.0.0:5000->5000/tcp
```

---

## 6. Visualizar os logs

Para visualizar as mensagens geradas pela aplicação:

```bash
sudo docker logs meu-flask
```

Para acompanhar os logs em tempo real:

```bash
sudo docker logs -f meu-flask
```

---

# Acesso à Aplicação

Com o contêiner em execução, a aplicação pode ser acessada através de um navegador.

Utilizando o endereço IP da máquina virtual:

```text
http://IP_DA_VM:5000
```

Por exemplo:

```text
http://192.168.0.7:5000
```

> O endereço IP utilizado deve ser substituído pelo endereço IP atual da máquina virtual Ubuntu Server.

---

## Rotas Disponíveis

### Página inicial

```text
http://IP_DA_VM:5000/
```

### Página do segredo

```text
http://IP_DA_VM:5000/segredo
```

### Página dos membros

```text
http://IP_DA_VM:5000/membros
```

---

# Atualização da Aplicação

Quando o arquivo `app.py` é alterado, a imagem Docker existente não é atualizada automaticamente.

É necessário reconstruir a imagem e recriar o contêiner.

## 1. Construir novamente a imagem

```bash
sudo docker build --no-cache -t minha-flask .
```

A opção `--no-cache` força a reconstrução das etapas da imagem sem utilizar o cache anterior.

## 2. Parar o contêiner atual

```bash
sudo docker stop meu-flask
```

## 3. Remover o contêiner antigo

```bash
sudo docker rm meu-flask
```

## 4. Criar um novo contêiner

```bash
sudo docker run -d -p 5000:5000 --name meu-flask minha-flask
```

## 5. Verificar

```bash
sudo docker ps
```

Depois disso, acesse novamente:

```text
http://IP_DA_VM:5000
```

---

# Comandos Úteis

### Listar contêineres em execução

```bash
sudo docker ps
```

### Listar todos os contêineres

```bash
sudo docker ps -a
```

### Listar imagens

```bash
sudo docker images
```

### Parar o contêiner

```bash
sudo docker stop meu-flask
```

### Iniciar novamente o contêiner

```bash
sudo docker start meu-flask
```

### Reiniciar o contêiner

```bash
sudo docker restart meu-flask
```

### Remover o contêiner

```bash
sudo docker rm meu-flask
```

### Visualizar os logs

```bash
sudo docker logs meu-flask
```

---

# Verificação da Porta

Caso a aplicação não seja acessível pelo navegador, é possível verificar se a porta 5000 está sendo utilizada:

```bash
sudo ss -tulpn | grep 5000
```

O resultado esperado é semelhante a:

```text
tcp LISTEN 0 4096 0.0.0.0:5000 0.0.0.0:*
```

Isso indica que a porta 5000 está sendo utilizada pelo Docker.

---

# Repositório Base

O projeto foi desenvolvido com base nos materiais e referências fornecidos para a disciplina, utilizando Docker para executar a aplicação Flask em um ambiente de servidor.

---

# Conclusão

O projeto demonstra a utilização do **Docker para executar uma aplicação web desenvolvida em Python com Flask**, permitindo que a aplicação seja isolada em um contêiner e acessada através da rede utilizando a porta 5000.

O processo envolve:

1. Criação da aplicação Flask.
2. Definição das dependências no `requirements.txt`.
3. Criação do `Dockerfile`.
4. Construção da imagem Docker.
5. Criação e execução do contêiner.
6. Acesso à aplicação através do endereço IP do servidor.
7. Atualização da aplicação através da reconstrução da imagem.
