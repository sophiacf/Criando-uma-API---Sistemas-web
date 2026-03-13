from flask import Flask, jsonify;
import os

app = Flask(__name__)

filmes = [
    {"id": 1, "filme": "Titanic"},
    {"id": 2, "filme": "Romeu e Julieta"},
    {"id": 3, "filme": "Matrix"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de filmes - Acesse /filmes"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
