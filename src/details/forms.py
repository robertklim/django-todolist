from django import forms

from todos.models import Todos

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
    
    def __init__(self, user=None, *args, **kwargs):
        super(DetailsCreateForm, self).__init__(*args, **kwargs)
        # Filter by user and exclude todos that already have details
        self.fields['todo'].queryset = Todos.objects.filter(user=user).exclude(details__isnull=False)