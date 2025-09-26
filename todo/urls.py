from django.urls import path

from todo import views

urlspatterns = [
    path('', views.todo_list, name='todo_list'),
]