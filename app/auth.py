from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta

auth = Blueprint('auth', __name__)  # Create a blueprint for authentication

# Configuration (in a real app, use Flask app config or environment variables)
SECRET_KEY = "your_secret_key"  # Change this to a strong, unique secret key
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_SECONDS = 3600  # Token validity in seconds

# Dummy user for demonstration
USER_DATA = {
    "username": "test_user",
    "password": "plain_text_password"  # Assume plaintext for simplicity
}

def verify_user(username, password):
    """Verify user credentials. Replace with database validation in production."""
    return username == USER_DATA["username"] and password == USER_DATA["password"]

@auth.route('/login', methods=['POST'])
def login():
    """Login route for user authentication."""
    data = request.json
    if not data or not verify_user(data.get('username'), data.get('password')):
        return jsonify({"message": "Invalid credentials"}), 401

    # Create JWT token
    payload = {
        "user_id": 1,  # Example user ID
        "username": data.get('username'),
        "exp": datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION_SECONDS)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

    return jsonify({"token": token})
