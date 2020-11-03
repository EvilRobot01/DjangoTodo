from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, ListContainer
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

def list_update(request, list_id):
    #get single item
    container  = ListContainer.objects.get(id=list_id)
    #update item
    container_form = ListContainerModelForm(request.POST or None, instance=container)
    context = {
        'container_form':container_form
    }
    template = 'list_container/list-update.html'
    if request.method == 'POST':
        if container_form.is_valid():
            new_task = container_form.save(commit=False )
            new_task.save()
        return redirect('/')
    return render(request, template, context)

def list_delete(request, list_id):
    #get single item
    container = ListContainer.objects.get(id=list_id)
    context = {
        'container':container
    }
    template = 'list_container/list-delete.html'
    #delete item
    if request.method == 'POST':
        container.delete()
        return redirect('/')
    return render(request, template, context)
    

def container(request, container_id):
    #list all items
    contained_items = Task.objects.all().filter(list_container=container_id)
    #create new item
    task_form = TaskModelForm(request.POST or None)
    if request.method == 'POST':
        if task_form.is_valid():
            new_task = task_form.save(container_id, commit=False )
            new_task.save()
        return redirect(f'/item-list/{container_id}')
    return render(request, 'list_container/item-list.html', {'contained_items': contained_items, 'task_form':task_form})


def item_details(request, item_id):
    item = Task.objects.get(id=item_id)
    context = {
        'item': item,
    }
    template = 'list_container/item-detail.html'
    return render(request, template, context)


def item_update(request, item_id):
    #get single item
    item = Task.objects.get(id=item_id)
    #update item
    task_form = TaskModelForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if task_form.is_valid():
            new_task = task_form.save(item.list_container.id, commit=False )
            new_task.save()
        return redirect(f'/item-list/{item.list_container.id}')
    context = {
        'task_form':task_form
    }
    template = 'list_container/item-update.html'
    return render(request, template, context)

def item_delete(request, item_id):
    #get single item
    item = Task.objects.get(id=item_id)
    context = {
        'item':item
    }
    template = 'list_container/item-delete.html'
    #delete item
    if request.method == 'POST':
        item.delete()
        return redirect(f'/item-list/{item.list_container.id}')
    return render(request, template, context)