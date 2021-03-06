from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

#para definir que teremos vários caminhos auqi
auth = Blueprint('auth', __name__)

#Chamar as páginas
@auth.route('/login', methods = ['GET','POST'])
def login():#bom chamar do mesmo nome da root
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #procurando por algo especifico
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                #faz o usuario permanecer logado até o browser ser atualizado
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.' , category = 'error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
#obrigando o user estar logado para fazer o resto
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category ='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category ='error')
        elif password1!= password2:
            flash('Passwords don\'t match.', category ='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category ='error')
        else:
            #add user to databases
            new_user = User(email=email, first_name=first_name,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            #commit to database
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user = current_user)