from faker import Faker
from app import app, db  # Import your Flask app and SQLAlchemy instance from app.py
from models import Message  # Import your SQLAlchemy models from models.py

def make_messages():
    fake = Faker()

    with app.app_context():  # Use app.app_context() to ensure the Flask app context
        db.create_all()
        Message.query.delete()

        for _ in range(10):
            content = fake.text()
            message = Message(content=content)
            db.session.add(message)

        db.session.commit()

if __name__ == '__main__':
    make_messages()
