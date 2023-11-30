from flask import Flask

# Routes
from .routes import MetaTraderRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(MetaTraderRoutes.main, url_prefix='/mt5')

    return app