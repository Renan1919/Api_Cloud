from flask import Flask, jsonify

app = Flask(__name__)

# Rota raiz
@app.route("/")
def home():
    return "✅ API rodando! Use /alunos ou /saudacao/<nome>"

# Rota que retorna lista de alunos em JSON
@app.route("/alunos")
def get_alunos():
    return jsonify([
        {"nome": "John", "curso": "ADS"},
        {"nome": "Robson", "curso": "CC"}
    ])

# Exemplo de rota dinâmica (saudação)
@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify({"mensagem": f"Olá, {nome}! Bem-vindo à API 🚀"})

# 🚀 Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
