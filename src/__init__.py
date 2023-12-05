from flask import Flask

# Routes
from .routes import MetaTraderRoutes
from .routes import IndexRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(MetaTraderRoutes.main, url_prefix='/mt5')

    return app