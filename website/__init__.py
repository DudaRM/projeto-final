#Para rodar de forma automática usamos esse __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#criando database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'projeto teste'
    #configurar database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #segurança do app
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') #sem prefixo

    from .models import User, Note

    create_database(app)

    return app

#criando database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
