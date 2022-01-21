from flask import Blueprint
#para definir que teremos vários caminhos auqi

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():#bom chamar do mesmo nome da root
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup')
def signup():
    return "<p>Sign Up</p>"
