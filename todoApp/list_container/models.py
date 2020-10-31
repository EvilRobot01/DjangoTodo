from django.db import models
import datetime

# Create your models here.
class ListContainer(models.Model):

    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=100, 
                            unique=True,
                            error_messages={'unique': 'This title is not unique, please try again'},
                            help_text='Must be a unique title',
                            )

class Task(models.Model):

    def __str__(self):
        return self.item_name
    
    list_container = models.ForeignKey(ListContainer,  on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=100, 
                                unique=True, 
                                error_messages={'unique': 'This title is not unique, please try again'},
                                help_text='Must be a unique title',
                                    )
    details = models.TextField(null=True, blank=True, max_length=10000)
    date = models.DateField(default=datetime.date.today)

