from flask import Blueprint, render_template
#para definir que teremos vários caminhos auqi

views = Blueprint('views', __name__)

@views.route('/')
#para rodar a página home assim que encontrar o sinal / (route)
def home():
    return render_template("home.html")#pra retornar a pagina
