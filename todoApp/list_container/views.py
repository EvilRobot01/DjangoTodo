from django.shortcuts import render
from .models import Task, ListContainer
from django.shortcuts import render, redirect
from .forms import ListContainerModelForm

# Create your views here.

def index(request):
    list_container = ListContainer.objects.all()
    #Create new container
    form = ListContainerModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
        return redirect('/')
    return render(request, 'list_container/index.html', {'list_container': list_container, 'form':form})
    

def check_contained_items(request, container_id):
    contained_items = Task.objects.all().filter(list_container=container_id)
    return render(request, 'list_container/item_list.html', {'contained_items': contained_items})


