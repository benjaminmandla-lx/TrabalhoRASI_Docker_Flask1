from flask import Flask
import os
import mysql.connector

app = Flask(__name__)


def conectar_banco():
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )


@app.route("/")
def home():
    return """
    <h1>Bem-vindo ao Super Flask</h1>
    <p>Ele está sendo aplicado com o Docker, acredita?</p>
    <p>
        <a href="/sobre">Sobre</a> |
        <a href="/contato">Contato</a> |
        <a href="/alunos">Alunos</a>
    </p>
    """


@app.route("/sobre")
def sobre():
    return """
    <h1>Sobre o Projeto</h1>
    <p>
        O projeto Super Flask foi feito por alunos para professores de RASI
        e utiliza Python, Flask, MySQL e Docker.
    </p>
    <p>
        Este projeto foi feito pela Leticia e pelo Benjamin Mandla.
        Para tirar dúvidas, procure a barra de contato.
    </p>
    """


@app.route("/contato")
def contato():
    return """
    <h1>Contatos</h1>
    <p>
        Os contatos foram retirados por motivo de segurança.
        Tente novamente mais tarde.
    </p>
    """


@app.route("/alunos")
def alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("SELECT id, nome FROM alunos ORDER BY id")
        registros = cursor.fetchall()

        html = "<h1>Alunos cadastrados no MySQL</h1><ul>"

        for aluno in registros:
            html += f"<li>{aluno['id']} - {aluno['nome']}</li>"

        html += "</ul>"

        return html

    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
