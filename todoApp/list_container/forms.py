from django import forms
from .models import ListContainer, Task

class ListContainerModelForm(forms.ModelForm):
    class Meta:
        model = ListContainer
        fields = [
            'title'
        ]