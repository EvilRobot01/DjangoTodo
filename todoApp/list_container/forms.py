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
            'quantity',
            'details',
            'date'
        ] 
    
    def save(self, container_id, commit=True):
        obj = super().save(commit=False)
        obj.list_container = ListContainer.objects.get(pk=container_id)
        if commit:
            obj.save()
        return obj