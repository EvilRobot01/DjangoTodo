from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    template = 'users/registration.html'
    #User form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username = form.cleaned_data.get('email')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('/')
    else:
        form = UserCreationForm()
    context ={
        'form':form
            }
            
    return render(request, template, context)