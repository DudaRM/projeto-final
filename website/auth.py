from flask import Blueprint, render_template
#para definir que teremos vários caminhos auqi

auth = Blueprint('auth', __name__)

#Chamar as páginas
@auth.route('/login')
def login():#bom chamar do mesmo nome da root
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")
