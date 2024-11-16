from .models import TodoItem
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title']
        labels = {
            'title': 'title',
        }