from django.shortcuts import render
from .forms import QuestionsForm

def index(request):
    form = QuestionsForm()
    context= {'form':form}
    return render(request, 'templates/quiz.html',context)

