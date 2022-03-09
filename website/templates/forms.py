from django.forms import ModelForm
from .models import Questions

class QuestionForm(ModelForm):
    model = Questions
    fields = '__all__'