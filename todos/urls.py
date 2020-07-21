"""TodoProject URL Configuration

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
import os
from django.urls import path, include
# import importlib.util
# views = importlib.util.spec_from_file_location("list_todo_item", "D:/Yokesh/python/todo/project/TodoProject/views.py")
from todos import views
from todos.views import ( ListTodoItem, InsertTodoItem )

urlpatterns = [
    path('registration/',views.registration_site,name='registration'),
    path('login/',views.login_site,name='login'),
    path('list/', ListTodoItem.as_view()),
    # path('list/', views.list_todo_item),
    path('insert_todo/',InsertTodoItem.as_view(),name='insert_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_item'),
]
