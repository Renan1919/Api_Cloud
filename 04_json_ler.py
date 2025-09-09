from flask import Flask

# Cria aplicação Flask
app = Flask(__name__)

# Define rota inicial
@app.route("/")
def home():
    return "Minha primeira API com Flask!"

# Executa servidor local
if __name__ == "__main__":
    app.run(debug=True)