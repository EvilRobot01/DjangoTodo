"""todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from list_container import views as list_container_views
from users import views as user_views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #list_container
    path('', list_container_views.index , name='index'),
    path('list-update/<int:list_id>', list_container_views.list_update , name='list-update'),
    path('list-delete/<int:list_id>', list_container_views.list_delete , name='list-delete'),
    path('item-list/<int:container_id>', list_container_views.container , name='item-list'),
    path('item-details/<int:item_id>', list_container_views.item_details , name='item-details'),
    path('item-update/<int:item_id>', list_container_views.item_update , name='item-update'),
    path('item-delete/<int:item_id>', list_container_views.item_delete , name='item-delete'),

    #users
    path('register/', user_views.register , name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html') , name='logout'),
]

