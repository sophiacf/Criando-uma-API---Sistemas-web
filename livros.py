from flask import Flask, jsonify;
import os

app = Flask(__name__)

livros = [
    {"id": 1, "livro": "A menina que roubava livros"},
    {"id": 2, "livro": "Pequeno principe"},
    {"id": 3, "livro": "Bela e a Fera"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /livros"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(livros)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
