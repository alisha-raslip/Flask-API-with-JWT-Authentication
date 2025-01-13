from flask import Flask
from .auth import auth
from .routes import routes

def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.register_blueprint(auth, url_prefix='/api')  # Register auth blueprint
    app.register_blueprint(routes, url_prefix='/api')  # Register routes blueprint
    return app
