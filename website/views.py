from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
#para definir que teremos vários caminhos auqi

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
#para rodar a página home assim que encontrar o sinal / (route)

#Add notas
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
             flash('Note is too short', category='error')
        else:
            new_note = Note(data=note,user_id=current_user.id)
            #add no bd
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!',category='success')

    return render_template("home.html" , user=current_user)#pra retornar a pagina

@views.route('/delete-note', methods=['POST'])
#recebe a string do index.js, transforma em um objeto de dicionário python e então acessa o id da Note
 
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    #acessa a chave primária
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            #return a empty response
        
        return jsonify({})
