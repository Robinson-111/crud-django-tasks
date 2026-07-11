from django.shortcuts import render, redirect, get_object_or_404
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
    descripcion = request.POST['description'] 
    prioridad = 'important' in request.POST

    tarea = Task(title = titulo, description = descripcion, important = prioridad)
    tarea.save()

    return redirect('tasks')


def edit_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/edit_task.html')


def details_task(request, id):

    task = get_object_or_404(Task, id = id)
    return render(request, 'tasks/details_task.html', {
        'task': task
    })


def edit_task(request, id):
    if request.method == "GET":
        return render(request, 'tasks/edit_task.html')

    # task = Task.objects.get(id = id)






