from django.shortcuts import render
from .models import Task, ListContainer
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    list_container = ListContainer.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title', '')
        new_list = ListContainer(title=title)
        new_list.save()  
        return redirect('/')
    return render(request, 'list_container/index.html', {'list_container': list_container})

def check_contained_items(request, container_id):
    contained_items = Task.objects.all().filter(list_container=container_id)
    return render(request, 'list_container/item_list.html', {'contained_items': contained_items})


