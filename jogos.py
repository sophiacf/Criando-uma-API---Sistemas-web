from flask import Flask, jsonify;
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "jogo": "The sims 4"},
    {"id": 2, "jogo": "Alice in madness return"},
    {"id": 3, "jogo": "Stardew Valley"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
