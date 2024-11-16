from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("addtodo/", views.addtodo, name="addtodo"),
    path("deletetodo/<int:pk>", views.deletetodo, name="deletetodo"),
    path("editodo/<int:pk>", views.edittodo, name="edittodo"),
]
