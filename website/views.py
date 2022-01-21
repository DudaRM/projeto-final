from flask import Blueprint
#para definir que teremos vários caminhos auqi

views = Blueprint('views', __name__)

@views.route('/')
#para rodar a página home assim que encontrar o sinal / (route)
def home():
    return "<h1>Test</h1>"
