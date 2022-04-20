"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from myapp import views as myapp_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('login/', myapp_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', myapp_view.register, name ='register'),
    path('list_view/',myapp_view.list_view,name ='list_view'),
    path('detail_view/<id>',myapp_view.detail_view,name ='detail_view'),
    path('update_view/<id>',myapp_view.update_view,name = 'update_view'),
    path('delete_view/<id>',myapp_view.delete_view,name = 'delete_view'),
    path('home_view/',myapp_view.home_view,name = 'home_view'),
    path('data_view/',myapp_view.data_view,name = 'data_view'),
]
