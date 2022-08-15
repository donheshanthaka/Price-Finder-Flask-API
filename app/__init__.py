from flask import Flask

def create_app():

    app = Flask(__name__)

    # app.config.from_object("config.DevelopmentConfig")
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")

    elif app.config["ENV"] == "development":
        app.config.from_object("config.DevelopmentConfig")

    else:
        app.config.from_object("config.ProductionConfig")


    from app import views

    return app