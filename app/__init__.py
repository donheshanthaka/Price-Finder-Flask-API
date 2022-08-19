from flask import Flask
from app.views import views
from app.error_handlers import error_handlers

def create_app():

    app = Flask(__name__)

    # app.config.from_object("config.DevelopmentConfig")
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")

    elif app.config["ENV"] == "development":
        app.config.from_object("config.DevelopmentConfig")

    else:
        app.config.from_object("config.ProductionConfig")

    app.register_blueprint(views)
    app.register_blueprint(error_handlers)

    return app