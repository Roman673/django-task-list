from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/tasks.html', {
        'form': form,
        'tasks': Task.objects.all()
    })

def task_delete(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
    return redirect('tasks:tasks') 
