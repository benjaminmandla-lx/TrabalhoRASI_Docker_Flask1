# TrabalhoRASI_Docker_Flask1

# Docker com Aplicação Python/Flask
 
Projeto desenvolvido para a disciplina de Redes e Administração de Sistemas (RASI) do Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) - Campus Campos do Jordão.
 
## Objetivo
 
Este projeto tem como objetivo demonstrar a criação e execução de uma aplicação web desenvolvida em Python utilizando o framework Flask, executada dentro de um contêiner Docker.
 
## Estrutura do Projeto

projeto-flask/ │ ├── Dockerfile └── app/ ├── app.py └── requirements.txt


## Tecnologias Utilizadas

- Ubuntu Server
- Docker
- Python 3.14 Slim
- Flask

## Arquivo app.py

Aplicação Flask simples contendo uma página principal e duas rotas adicionais.

### Rotas disponíveis

| Rota | Descrição |
|--------|-------------|
| / | Página inicial |
| /segredo | Página temática sobre o segredo da empresa |
| /membros | Lista fictícia de membros da empresa |

## Requirements

Arquivo `requirements.txt`:

```txt
Flask==3.1.2

Dockerfile
Dockerfile
FROM python:3.14-slim
 
WORKDIR /app
 
COPY app/requirements.txt .
 
RUN pip install --no-cache-dir -r requirements.txt
 
COPY app/ .
 
EXPOSE 5000
 
CMD ["python", "app.py"]
Construção da Imagem

No diretório do projeto:

Shell
docker build -t minha-flask .
Execução do Contêiner
Shell
docker run -d -p 5000:5000 --name meu-flask minha-flask
Verificação

Listar contêineres em execução:

Shell
docker ps

Visualizar logs:

Shell
docker logs meu-flask
Acesso

Após iniciar o contêiner, acessar:

http://IP_DA_VM:5000

Rotas adicionais:

http://IP_DA_VM:5000/segredo
 
http://IP_DA_VM:5000/membros
Atualização da Aplicação

Sempre que o arquivo app.py for alterado, é necessário reconstruir a imagem Docker:

Shell
docker build --no-cache -t minha-flask .
 
docker stop meu-flask
 
docker rm meu-flask
 
docker run -d -p 5000:5000 --name meu-flask minha-flask
Repositório Base

Repositório utilizado como referência:

https://github.com/CesarAugusto88/RAS-Docker
