from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash

#para definir que teremos vários caminhos auqi

auth = Blueprint('auth', __name__)

#Chamar as páginas
@auth.route('/login', methods = ['GET','POST'])
def login():#bom chamar do mesmo nome da root
    data = request.form
    print(data)
    return render_template("login.html", text="Testing", user="Tim")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category ='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category ='error')
        elif password1!= password2:
            flash('Passwords don\'t match.', category ='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category ='error')
        else:
            #add user to databases
            new_user = User(email=email, firstName=firstName,password=generate_password_hash(password1, method='sha256'))
            flash('Account created!', category='success')

    return render_template("sign_up.html")
