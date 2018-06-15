from django import forms

from .models import Details

class DetailsCreateForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = [
            'todo',
            'keywords',
            'description',
            'public',
        ]