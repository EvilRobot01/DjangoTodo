from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    template = 'users/registration.html'
    #User form
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    context ={
        'form':form
            }
            
    return render(request, template, context)