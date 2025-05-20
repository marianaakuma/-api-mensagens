from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = {
    1: {"id": 1, "name": "joao"},
    2: {"id": 2, "name": "ana"},
}

def response_user():
    return jsonify({"users": list(users_data.values())})

@app.route("/")
def root():
    return 'mensagem 1'

@app.route("/users", methods=["GET"])
def list_users():
    return response_user()

@app.route("/users", methods=["POST"])
def create_users():
    body = request.json

    ids = list(users_data.keys())

    if ids: 
        new_id = max(ids) + 1  
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "name": body["name"]
    }

    return jsonify({"message": "Usuário criado com sucesso!", "user": users_data[new_id]})


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete(user_id:int):
    user = users_data.get(user_id)

    if user:
        del users_data.get(user_id)



if __name__ == '__main__':
    app.run(debug=True)
