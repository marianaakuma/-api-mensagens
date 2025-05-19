from flask import Blueprint, request, jsonify, abort
from ..models.message import Message
from .. import db

messages_bp = Blueprint('messages', __name__)

# Rota para listar todas as mensagens
@messages_bp.route('/', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([msg.to_dict() for msg in messages]), 200

# Rota para obter uma mensagem por id
@messages_bp.route('/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get_or_404(message_id)
    return jsonify(message.to_dict()), 200

# Rota para criar uma nova mensagem
@messages_bp.route('/', methods=['POST'])
def create_message():
    data = request.get_json()
    if not data or 'content' not in data:
        abort(400, description="Campo 'content' é obrigatório.")

    new_message = Message(content=data['content'])
    db.session.add(new_message)
    db.session.commit()

    return jsonify(new_message.to_dict()), 201

# Rota para atualizar uma mensagem existente
@messages_bp.route('/<int:message_id>', methods=['PUT'])
def update_mensagem(id_mensagem):
    # Busca a mensagem ou retorna 404 se não existir
    mensagem = Mensagem.query.get_or_404(id_mensagem)

    # Obtém o JSON enviado pelo cliente
    data = request.get_json()

    # Valida e atualiza o objeto existente usando o schema
    dados_atualizados = mensagem_schema.load(
        data,
        instance=mensagem,  # indica que é um update
        partial=True         # permite omissão de campos
    )

    # Persiste a alteração no banco
    db.session.commit()

    # Retorna a mensagem atualizada
    return mensagem_schema.jsonify(dados_atualizados), 200

# Rota para deletar uma mensagem
@messages_bp.route('/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()

    return '', 204