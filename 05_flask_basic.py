from flask import Flask

# Cria aplicação Flask - inicia aplicacao do flask
app = Flask(__name__)

# Define rota inicial - é a raiz da api
@app.route("/")
def home():
    return "Minha primeira API com Flask!"

# Executa servidor local app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)