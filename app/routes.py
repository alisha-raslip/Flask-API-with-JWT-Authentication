from flask import Blueprint, request, jsonify
import jwt

routes = Blueprint('routes', __name__)  # Create a blueprint for routes

# Configuration (should match auth.py)
SECRET_KEY = "your_secret_key"
JWT_ALGORITHM = "HS256"

def token_required(request):
    """Verify the presence and validity of a JWT token."""
    token = request.headers.get('Authorization')
    if not token:
        return {"message": "Token is missing"}, 401

    try:
        # Decode the token
        decoded_token = jwt.decode(token.split("Bearer ")[-1], SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token  # Return payload if the token is valid
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}, 401

@routes.route('/protected', methods=['GET'])
def protected():
    """A protected route that requires a valid JWT token."""
    token_verification = token_required(request)
    if isinstance(token_verification, tuple):  # Error tuple returned
        return jsonify(token_verification[0]), token_verification[1]

    return jsonify({"message": "Access granted", "data": token_verification})
