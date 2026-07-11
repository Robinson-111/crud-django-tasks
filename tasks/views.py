from django.shortcuts import render, redirect
from .models import Task

def tasks(request):

    task = Task.objects.all()

    return render(request, 'tasks/tasks.html',{
        'tasks': task
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html')
    
    titulo = request.POST['title']
    descripcion = request.POST['description']        # prioridad = request.POST['important']

    tarea = Task(title = titulo, description = descripcion)
    tarea.save()

    return redirect('tasks')


def edit_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/edit_task.html')


