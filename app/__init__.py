from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.json.sort_keys = False

    db.init_app(app)
    ma.init_app(app)

    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix="/messages")

    # Tratadores globais de erro (explicados na seção 5.6)
    register_error_handlers(app)

    return app