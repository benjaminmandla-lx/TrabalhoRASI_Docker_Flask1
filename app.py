from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
        <h1>Bem vindo ao super Flask</h1>
        <p>Ele esta sendo aplicado com o Docker, acredita?</p>
    """


@app.route("/segredo")
def segredo():
    return """
        <style>
            body {
                background: #111;
                color: #0f0;
                text-align: center;
            }
        </style>

        <h2>Você descobriu a verdade da empresa, ela e comandada por aliens!!!</h2>
    """


@app.route("/membros")
def membros():
    return """
        <style>
            body {
                color: darkblue;
            }
        </style>

        <h1>Estes sao os membros da Empresa:</h1>
        <p>Humano Bilú</p>
        <p>Barry Allen</p>
        <p>E. T. Souza</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
