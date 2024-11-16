from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .models import TodoItem
from .forms import TodoForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items=TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def edittodo(request, pk):
    todo=TodoItem.objects.get(pk= pk)
    form = TodoForm(request.POST, instance=todo)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse("Todos"))
    return render(request, 'edittodo.html', {'form': TodoForm(instance=todo)})
        


def addtodo(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_title = form.cleaned_data['title']
            new_todo = TodoItem(title=new_title)
            new_todo.save()
            return HttpResponseRedirect(reverse("Todos"))


        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse("Todos"))

    return render(request, "addtodo.html", {"form": form})

def deletetodo(request, pk):
    todo=TodoItem.objects.get(pk= pk)
    todo.delete()
    return HttpResponseRedirect(reverse("Todos"))

