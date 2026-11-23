# TrabalhoRASI_Docker_Flask1

# Docker com Aplicação Python/Flask

Projeto desenvolvido para a disciplina de **Redes e Administração de Sistemas (RASI)** do **Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) — Campus Campos do Jordão**.

---

## Objetivo

Este projeto tem como objetivo demonstrar a criação, configuração e execução de uma aplicação web desenvolvida em **Python utilizando o framework Flask**, executada em contêineres Docker em um ambiente **Ubuntu Server**.

O trabalho apresenta duas etapas principais:

1. Criação e execução de uma aplicação Flask em um contêiner Docker.
2. Ampliação da aplicação utilizando Docker Compose, integrando Flask, MySQL e Apache.

A aplicação disponibiliza diferentes páginas, permite a consulta de alunos armazenados em um banco de dados MySQL e utiliza o Apache como servidor intermediário para receber as requisições HTTP.

---

# Etapa 1 — Aplicação Flask com Docker

## Tecnologias utilizadas

- **Ubuntu Server** — sistema operacional utilizado no ambiente do servidor.
- **Docker** — plataforma utilizada para criação e execução dos contêineres.
- **Python 3.14 Slim** — imagem base utilizada no contêiner.
- **Flask 3.1.2** — framework utilizado para desenvolvimento da aplicação web.

## Estrutura inicial do projeto

A estrutura inicial do projeto foi organizada da seguinte maneira:

```text
projeto-flask/
├── Dockerfile
└── app/
    ├── app.py
    └── requirements.txt
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `Dockerfile` | Define as instruções utilizadas para criar a imagem Docker. |
| `app/app.py` | Contém o código da aplicação Flask e suas rotas. |
| `app/requirements.txt` | Lista as dependências Python utilizadas pela aplicação. |

## Requirements

Inicialmente, o arquivo `requirements.txt` continha a dependência necessária para executar a aplicação:

```txt
Flask==3.1.2
```

## Dockerfile

O Dockerfile utilizado na primeira etapa foi:

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

- `FROM python:3.14-slim` — utiliza uma imagem compacta do Python 3.14 como base.
- `WORKDIR /app` — define `/app` como diretório de trabalho dentro do contêiner.
- `COPY app/requirements.txt .` — copia o arquivo de dependências para o contêiner.
- `RUN pip install --no-cache-dir -r requirements.txt` — instala as dependências da aplicação.
- `COPY app/ .` — copia os arquivos da aplicação para o contêiner.
- `EXPOSE 5000` — informa que a aplicação utiliza a porta 5000.
- `CMD ["python", "app.py"]` — inicia a aplicação Flask quando o contêiner é executado.

## Execução da primeira etapa

### 1. Verificar o Docker

Antes de iniciar o projeto, verifique se o Docker está instalado:

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

### 2. Acessar o diretório do projeto

```bash
cd ~/projeto-flask
```

A estrutura pode ser conferida com:

```bash
find . -maxdepth 2 -type f
```

### 3. Construir a imagem Docker

No diretório que contém o Dockerfile, execute:

```bash
sudo docker build -t minha-flask .
```

Para verificar se a imagem foi criada:

```bash
sudo docker images
```

### 4. Executar o contêiner

```bash
sudo docker run -d -p 5000:5000 --name meu-flask minha-flask
```

Explicação:

- `-d` — executa o contêiner em segundo plano.
- `-p 5000:5000` — conecta a porta 5000 da máquina à porta 5000 do contêiner.
- `--name meu-flask` — define o nome do contêiner.
- `minha-flask` — nome da imagem utilizada.

### 5. Verificar o contêiner

```bash
sudo docker ps
```

O resultado deverá apresentar o contêiner `meu-flask` em execução e a porta:

```text
0.0.0.0:5000->5000/tcp
```

### 6. Visualizar os logs

```bash
sudo docker logs meu-flask
```

Para acompanhar os logs em tempo real:

```bash
sudo docker logs -f meu-flask
```

### 7. Acessar a aplicação

Com o contêiner em execução, a aplicação pode ser acessada através de um navegador:

```text
http://IP_DA_VM:5000
```

O endereço IP deve ser substituído pelo endereço atual da máquina virtual Ubuntu Server.

---

# Etapa 2 — Integração com MySQL e Apache utilizando Docker Compose

## Objetivo da segunda etapa

Na segunda etapa, a aplicação foi ampliada para utilizar uma arquitetura com três serviços independentes:

- **Flask:** responsável pelo funcionamento da aplicação web.
- **MySQL:** responsável pelo armazenamento dos dados dos alunos.
- **Apache:** responsável por receber as requisições HTTP e encaminhá-las para a aplicação Flask.

Para organizar e executar os serviços em conjunto, foi utilizado o **Docker Compose**.

Essa organização permite que os contêineres sejam configurados e iniciados por meio de um único arquivo de configuração.

## Tecnologias utilizadas

- **Ubuntu Server** — ambiente de execução do projeto.
- **Docker** — criação e execução dos contêineres.
- **Docker Compose** — orquestração dos serviços.
- **Python 3.14 Slim** — imagem base da aplicação.
- **Flask 3.1.2** — framework web.
- **MySQL 8.0** — sistema gerenciador de banco de dados.
- **Apache HTTP Server 2.4** — servidor HTTP e proxy reverso.

## Estrutura final do projeto

A estrutura final do projeto é organizada da seguinte maneira:

```text
projeto-flask/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── compose.yaml
├── .env
├── .gitignore
└── httpd.conf
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `app/app.py` | Contém a aplicação Flask, suas rotas e a conexão com o MySQL. |
| `app/requirements.txt` | Lista as dependências Python. |
| `Dockerfile` | Define como construir a imagem da aplicação Flask. |
| `compose.yaml` | Configura e organiza os três serviços Docker. |
| `.env` | Armazena as variáveis de ambiente e as senhas do banco de dados. |
| `.gitignore` | Define arquivos que não devem ser enviados ao Git. |
| `httpd.conf` | Configura o Apache e o encaminhamento das requisições para o Flask. |

## 1. Requirements

O arquivo `app/requirements.txt` contém as dependências necessárias:

```txt
Flask==3.1.2
mysql-connector-python
```

- `Flask` — framework utilizado para desenvolver a aplicação.
- `mysql-connector-python` — biblioteca responsável pela comunicação entre Python e MySQL.

## 2. Dockerfile

O Dockerfile utilizado para construir a imagem da aplicação Flask é:

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

O funcionamento das instruções permanece o mesmo da primeira etapa, porém agora a imagem também instala a biblioteca necessária para conectar a aplicação ao MySQL.

## 3. Variáveis de ambiente

Foi criado um arquivo `.env` para armazenar as senhas utilizadas pelo MySQL.

Exemplo de estrutura:

```env
MYSQL_ROOT_PASSWORD=sua_senha_root
MYSQL_PASSWORD=sua_senha_flask
```

As senhas devem ser substituídas por valores definidos pelo responsável pelo projeto.

O arquivo `.env` permite separar informações sensíveis dos arquivos principais de configuração.

Para restringir o acesso ao arquivo:

```bash
chmod 600 .env
```

O arquivo também deve ser incluído no `.gitignore`, evitando que as senhas sejam enviadas ao repositório.

## 4. Configuração do Git

O arquivo `.gitignore` contém:

```gitignore
.env
__pycache__/
*.pyc
```

Essas regras evitam o envio de arquivos com informações sensíveis e arquivos temporários do Python.

## 5. Configuração do Docker Compose

O arquivo `compose.yaml` define os três serviços utilizados no projeto:

```yaml
services:
  db:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:?Defina no .env}
      MYSQL_DATABASE: meu_banco
      MYSQL_USER: flaskuser
      MYSQL_PASSWORD: ${MYSQL_PASSWORD:?Defina no .env}
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h 127.0.0.1 -uroot -p\"$${MYSQL_ROOT_PASSWORD}\" --silent"]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 30s

  flask:
    build:
      context: .
    restart: unless-stopped
    environment:
      DB_HOST: db
      DB_PORT: "3306"
      DB_NAME: meu_banco
      DB_USER: flaskuser
      DB_PASSWORD: ${MYSQL_PASSWORD:?Defina no .env}
    volumes:
      - ./app:/app
    expose:
      - "5000"
    depends_on:
      db:
        condition: service_healthy

  server:
    image: httpd:2.4
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - ./httpd.conf:/usr/local/apache2/conf/httpd.conf:ro
    depends_on:
      - flask

volumes:
  mysql_data:
```

### Funcionamento dos serviços

**Serviço db — MySQL**

- Utiliza a imagem oficial `mysql:8.0`.
- Cria o banco de dados `meu_banco`.
- Cria o usuário `flaskuser`.
- Recebe as senhas por meio das variáveis de ambiente.
- Utiliza o volume `mysql_data` para armazenar os dados.
- Possui um healthcheck para verificar se o banco está pronto para receber conexões.

**Serviço flask — Aplicação Flask**

- Constrói sua imagem utilizando o Dockerfile do projeto.
- Recebe as configurações de conexão com o MySQL.
- Utiliza o nome `db` como endereço do banco de dados dentro da rede Docker.
- Aguarda o MySQL ficar saudável antes de iniciar.
- Disponibiliza a porta 5000 internamente por meio de `expose`.

**Serviço server — Apache**

- Utiliza a imagem oficial `httpd:2.4`.
- Disponibiliza a porta 80 da máquina para acesso externo.
- Utiliza o arquivo `httpd.conf` como configuração.
- Encaminha as requisições recebidas para o serviço Flask.

## 6. Configuração do Apache

O arquivo `httpd.conf` configura o Apache para funcionar como um proxy reverso.

```apache
ServerRoot "/usr/local/apache2"
Listen 80
ServerName localhost

LoadModule mpm_event_module modules/mod_mpm_event.so
LoadModule authz_core_module modules/mod_authz_core.so
LoadModule unixd_module modules/mod_unixd_module.so
LoadModule log_config_module modules/mod_log_config.so
LoadModule mime_module modules/mod_mime_module.so
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so

User daemon
Group daemon

TypesConfig conf/mime.types

ErrorLog /proc/self/fd/2
LogLevel warn
CustomLog /proc/self/fd/1 common

<VirtualHost *:80>
    ProxyRequests Off
    ProxyPreserveHost On
    ProxyPass / http://flask:5000/
    ProxyPassReverse / http://flask:5000/
</VirtualHost>
```

### Funcionamento da configuração

- `Listen 80` — define a porta em que o Apache recebe as requisições.
- `LoadModule proxy_module` — habilita o módulo de proxy.
- `LoadModule proxy_http_module` — permite encaminhar requisições HTTP.
- `ProxyRequests Off` — desabilita o proxy aberto.
- `ProxyPreserveHost On` — preserva o cabeçalho Host original.
- `ProxyPass / http://flask:5000/` — encaminha as requisições para o Flask.
- `ProxyPassReverse` — ajusta os cabeçalhos de redirecionamento recebidos do servidor de destino.

Dessa maneira, o usuário acessa a aplicação pela porta 80, enquanto o Apache encaminha as requisições internamente para a porta 5000 do Flask.

## 7. Aplicação Flask

O arquivo `app/app.py` contém a aplicação web e a função responsável pela conexão com o banco de dados.

### Conexão com o MySQL

A função `conectar_banco()` utiliza as variáveis de ambiente fornecidas pelo Docker Compose:

```python
def conectar_banco():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )
```

As configurações são obtidas por meio de variáveis de ambiente, evitando deixar as credenciais diretamente no código.

### Rotas disponíveis

| Rota | Descrição |
|---|---|
| `/` | Página inicial do Super Flask. |
| `/sobre` | Apresenta informações sobre o projeto. |
| `/contato` | Apresenta a página de contatos. |
| `/alunos` | Consulta e apresenta os alunos cadastrados no MySQL. |

### Consulta dos alunos

A rota `/alunos` utiliza uma consulta SQL para recuperar os registros armazenados:

```sql
SELECT id, nome FROM alunos ORDER BY id;
```

Os resultados são apresentados dinamicamente na página HTML.

## 8. Inicialização dos serviços

Antes de iniciar os contêineres, é necessário acessar o diretório do projeto:

```bash
cd ~/projeto-flask
```

### Validar a configuração

Para verificar se o arquivo Compose está corretamente configurado:

```bash
sudo docker compose config
```

Também é possível listar os serviços:

```bash
sudo docker compose config --services
```

O resultado esperado é:

```text
db
flask
server
```

### Construir e iniciar os serviços

Execute:

```bash
sudo docker compose up -d --build
```

O comando:

- `up` — cria e inicia os serviços.
- `-d` — executa os contêineres em segundo plano.
- `--build` — constrói ou atualiza as imagens necessárias antes de iniciar os serviços.

### Verificar os contêineres

```bash
sudo docker compose ps
```

Os três serviços devem aparecer em execução. O serviço MySQL deve apresentar o estado `healthy` quando estiver pronto.

### Consultar os logs

Para visualizar os logs de todos os serviços:

```bash
sudo docker compose logs
```

Para acompanhar os logs do Flask:

```bash
sudo docker compose logs -f flask
```

Para sair do acompanhamento dos logs, pressione `Ctrl + C`.

## 9. Criação da tabela no MySQL

Após iniciar os serviços, é necessário criar a tabela responsável por armazenar os alunos.

Para acessar o banco de dados:

```bash
sudo docker compose exec db mysql -u flaskuser -p meu_banco
```

O terminal solicitará a senha definida em `MYSQL_PASSWORD` no arquivo `.env`.

Após entrar no MySQL, execute:

```sql
CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);
```

Para inserir registros de teste:

```sql
INSERT INTO alunos (nome)
VALUES ('Ana'), ('Bruno'), ('Carla');
```

Para verificar os registros:

```sql
SELECT * FROM alunos;
```

Para sair do MySQL:

```sql
EXIT;
```

A tabela criada será utilizada pela rota `/alunos` da aplicação Flask.

## 10. Acesso à aplicação

Após a inicialização dos três serviços, a aplicação pode ser acessada pelo navegador utilizando o endereço IP da máquina virtual:

```text
http://IP_DA_VM
```

Por exemplo:

```text
http://192.168.0.7
```

O endereço IP deve ser substituído pelo endereço atual da máquina virtual Ubuntu Server.

Para descobrir o IP:

```bash
hostname -I
```

### Rotas disponíveis

**Página inicial**

```text
http://IP_DA_VM/
```

**Sobre o projeto**

```text
http://IP_DA_VM/sobre
```

**Contato**

```text
http://IP_DA_VM/contato
```

**Alunos cadastrados**

```text
http://IP_DA_VM/alunos
```

A página de alunos deverá apresentar os registros inseridos anteriormente no banco de dados MySQL.

## 11. Persistência dos dados

Para manter os registros mesmo após a remoção dos contêineres, foi configurado um volume Docker chamado `mysql_data`.

O volume é associado ao diretório de armazenamento do MySQL:

```yaml
volumes:
  - mysql_data:/var/lib/mysql
```

Isso permite que os dados permaneçam armazenados mesmo quando os contêineres são recriados.

### Verificar os registros antes de parar os serviços

```bash
sudo docker compose exec db mysql -u flaskuser -p meu_banco -e "SELECT * FROM alunos;"
```

### Parar e remover os contêineres

```bash
sudo docker compose down
```

### Iniciar novamente os serviços

```bash
sudo docker compose up -d
```

### Consultar os registros novamente

```bash
sudo docker compose exec db mysql -u flaskuser -p meu_banco -e "SELECT * FROM alunos;"
```

Os registros deverão continuar disponíveis, pois o volume `mysql_data` não foi removido.

**Importante:** o comando `docker compose down -v` remove também os volumes associados ao projeto e, consequentemente, pode apagar os dados armazenados no banco.

## 12. Atualização da aplicação

Quando o arquivo `app.py` é alterado, é possível reconstruir e atualizar os serviços com:

```bash
sudo docker compose up -d --build
```

Para visualizar os serviços após a atualização:

```bash
sudo docker compose ps
```

Para consultar os logs:

```bash
sudo docker compose logs flask
```

Como o diretório `./app` está associado ao diretório `/app` do contêiner por meio de um volume, as alterações nos arquivos da aplicação também ficam disponíveis dentro do contêiner. A reconstrução continua sendo importante quando houver mudanças nas dependências ou no Dockerfile.

---

# Comandos úteis do Docker Compose

### Listar os serviços

```bash
sudo docker compose ps
```

### Listar todos os contêineres, inclusive os encerrados

```bash
sudo docker compose ps -a
```

### Visualizar os logs

```bash
sudo docker compose logs
```

### Acompanhar os logs de um serviço

```bash
sudo docker compose logs -f flask
```

### Iniciar os serviços

```bash
sudo docker compose up -d
```

### Reconstruir e iniciar os serviços

```bash
sudo docker compose up -d --build
```

### Parar e remover os contêineres

```bash
sudo docker compose down
```

### Reiniciar os serviços

```bash
sudo docker compose restart
```

### Verificar os volumes

```bash
sudo docker volume ls
```

### Verificar as imagens

```bash
sudo docker images
```

---

# Verificação de portas

Caso a aplicação não seja acessível pelo navegador, é possível verificar se as portas estão sendo utilizadas:

```bash
sudo ss -tulpn | grep -E ':80|:5000|:3306'
```

Na arquitetura final:

- **Porta 80:** utilizada pelo Apache e disponibilizada para acesso externo.
- **Porta 5000:** utilizada internamente pela aplicação Flask.
- **Porta 3306:** utilizada internamente pelo MySQL.

A porta 5000 e a porta 3306 não precisam ser publicadas diretamente para a rede externa, pois a comunicação entre os serviços acontece pela rede interna criada pelo Docker Compose.

---

# Arquitetura final do projeto

A arquitetura final utiliza três contêineres que trabalham em conjunto:

```text
                 NAVEGADOR
                     |
                     |
                  PORTA 80
                     |
                     v
              +-------------+
              |    APACHE   |
              |   server    |
              +-------------+
                     |
                     |
              Rede Docker
                     |
                     v
              +-------------+
              |    FLASK    |
              |    flask    |
              +-------------+
                     |
                     |
              Rede Docker
                     |
                     v
              +-------------+
              |    MYSQL    |
              |      db     |
              +-------------+
                     |
                     |
                 mysql_data
                  (volume)
```

O fluxo de funcionamento ocorre da seguinte maneira:

1. O usuário acessa o endereço IP do servidor pelo navegador.
2. O Apache recebe a requisição pela porta 80.
3. O Apache encaminha a requisição para a aplicação Flask.
4. O Flask processa a solicitação.
5. Quando necessário, o Flask consulta o banco de dados MySQL.
6. O MySQL retorna os registros solicitados.
7. O Flask gera a resposta HTML.
8. O Apache encaminha a resposta de volta ao navegador.

---

# Repositório Base

O projeto foi desenvolvido com base nos materiais e orientações fornecidos para a disciplina de Redes e Administração de Sistemas (RASI), utilizando Docker para executar e organizar uma aplicação Flask em um ambiente Ubuntu Server.

---

# Conclusão

O trabalho demonstra a evolução de uma aplicação web simples para uma arquitetura composta por múltiplos serviços utilizando Docker e Docker Compose.

Na primeira etapa, foi desenvolvida uma aplicação Flask executada individualmente em um contêiner Docker.

Na segunda etapa, a aplicação foi ampliada com a integração de um banco de dados MySQL e um servidor Apache, utilizando o Docker Compose para organizar os serviços.

O projeto permitiu aplicar conceitos importantes de administração de sistemas, virtualização por contêineres, comunicação entre serviços, configuração de redes, armazenamento persistente e gerenciamento de aplicações web.

As principais atividades desenvolvidas foram:

1. Criação de uma aplicação utilizando Python e Flask.
2. Definição das dependências no `requirements.txt`.
3. Criação de imagens Docker por meio de um Dockerfile.
4. Execução e gerenciamento de contêineres.
5. Configuração de serviços utilizando Docker Compose.
6. Integração entre Flask e MySQL.
7. Configuração do Apache como proxy reverso.
8. Armazenamento persistente de dados por meio de volumes Docker.
9. Testes de funcionamento e acesso à aplicação pela rede.

Dessa forma, o projeto demonstra como diferentes tecnologias podem ser integradas para construir e executar uma aplicação web organizada em um ambiente de servidor.
