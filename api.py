from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = {
    1: {"id": 1, "name": "joao"},
    2: {"id": 2, "name": "ana"},
}

# Retorna todos os usuários
def response_user():
    return jsonify({"users": list(users_data.values())})

# Página inicial
@app.route("/")
def root():
    return 'mensagem 1'

# Listar todos os usuários
@app.route("/users", methods=["GET"])
def list_users():
    return response_user()

# Criar novo usuário
@app.route("/users", methods=["POST"])
def create_users():
    body = request.json
    ids = list(users_data.keys())
    new_id = max(ids) + 1 if ids else 1

    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }

    return jsonify({
        "message": "Usuário criado com sucesso!",
        "user": users_data[new_id]
    })

# Deletar usuário
@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    user = users_data.get(user_id)

    if user:
        del users_data[user_id]
        return jsonify({"message": f"Usuário {user_id} deletado com sucesso."})
    else:
        return jsonify({"error": "Usuário não encontrado."}), 404

# Atualizar usuário (opcional)
@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    user = users_data.get(user_id)

    if not user:
        return jsonify({"error": "Usuário não encontrado."}), 404

    body = request.json
    user["name"] = body.get("name", user["name"])
    return jsonify({"message": "Usuário atualizado com sucesso!", "user": user})

if __name__ == '__main__':
    app.run(debug=True)
