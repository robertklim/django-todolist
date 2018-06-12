from django import forms

from .models import Todos

class TodosCreateForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = [
            "title",
            "entry",
            "expires",
        ]