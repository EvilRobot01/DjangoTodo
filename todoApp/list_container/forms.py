from django import forms
from .models import ListContainer, Task

class ListContainerModelForm(forms.ModelForm):
    class Meta:
        model = ListContainer
        fields = [
            'title'
        ]

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task 

        fields = [

            'item_name',
            'details',
            'date'
        ] 
    
    def save(self, commit=True, *args, **kwargs):
        obj = super(TaskModelForm, self).save(commit=False, *args, **kwargs)
        #obj.list_container = container_id
        if commit:
            obj.save()
        return obj