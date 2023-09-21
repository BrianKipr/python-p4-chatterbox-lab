# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORS(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Message(db.Model):
#     __tablename__ = 'message'

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(255))

#     def serialize(self):
#         return {
#             'id': self.id,
#             'content': self.content,
#         }

# @app.route('/')
# def index():
#     return 'Hello, this is the root of the application!'

# @app.route('/messages', methods=['GET'])
# def get_messages():
#     messages = Message.query.all()
#     serialized_messages = [message.serialize() for message in messages]
#     return jsonify(serialized_messages)

# @app.route('/messages/<int:id>', methods=['GET'])
# def get_message_by_id(id):
#     message = Message.query.get(id)
#     if message:
#         serialized_message = message.serialize()
#         return jsonify(serialized_message)
#     else:
#         return jsonify({'message': 'Message not found'}), 404

# if __name__ == '__main__':
#     app.run(port=5555)




from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
        }

@app.route('/')
def index():
    return 'Hello, this is the root of the application!'

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    serialized_messages = [message.serialize() for message in messages]
    return jsonify(serialized_messages)

@app.route('/messages/<int:id>', methods=['GET'])
def get_message_by_id(id):
    message = Message.query.get(id)
    if message:
        serialized_message = message.serialize()
        return jsonify(serialized_message)
    else:
        return jsonify({'message': 'Message not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)

