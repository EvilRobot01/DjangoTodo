from django.shortcuts import render
from .models import Task, ListContainer
from django.shortcuts import render, redirect
from .forms import ListContainerModelForm, TaskModelForm

# Create your views here.

def index(request):
    #list all containers
    list_container = ListContainer.objects.all()
    #Create new container
    container_form = ListContainerModelForm(request.POST or None)
    if request.method == 'POST':
        if container_form.is_valid():
            new_container = container_form.save(commit=False)
            new_container.save()
        return redirect('/')
    return render(request, 'list_container/index.html', {'list_container': list_container, 'container_form':container_form})
    

def container(request, container_id):
    #list all items
    contained_items = Task.objects.all().filter(list_container=container_id)
    #create new item
    task_form = TaskModelForm(request.POST or None)
    if request.method == 'POST':
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.list_container = container_id
            new_task.save()
        return redirect('/')
    return render(request, 'list_container/item_list.html', {'contained_items': contained_items, 'task_form':task_form})


