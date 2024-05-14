from flask import jsonify, request
from app import app, db
from models import Chat, Message

# Get all chats or create a new chat
@app.route('/chats', methods=['GET', 'POST'])
def chats():
    if request.method == 'GET':
        chats_list = Chat.query.all()
        return jsonify([chat.name for chat in chats_list])
    elif request.method == 'POST':
        chat_name = request.json.get('name')
        new_chat = Chat(name=chat_name)
        db.session.add(new_chat)
        db.session.commit()
        return jsonify({'message': 'Chat created successfully'})

# Get all messages of a specific chat or send a new message
@app.route('/chats/<int:chat_id>/messages', methods=['GET', 'POST'])
def chat_messages(chat_id):
    if request.method == 'GET':
        messages_list = Message.query.filter_by(chat_id=chat_id).all()
        return jsonify([{'id': msg.id, 'text': msg.text} for msg in messages_list])
    elif request.method == 'POST':
        message_text = request.json.get('text')
        new_message = Message(text=message_text, chat_id=chat_id)
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'message': 'Message sent successfully'})

# Route to clear all chats
@app.route('/clear-chats', methods=['POST'])
def clear_chats():
    # Clear all chats from the database
    Chat.query.delete()
    db.session.commit()
    return jsonify({'message': 'All chats cleared successfully'})