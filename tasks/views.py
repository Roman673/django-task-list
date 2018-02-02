from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            messages.success(request, 'Added a new task {}.'.format(new_task))
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
        messages.success(request, 'Deleted task {}.'.format(task))
    return redirect('tasks:tasks') 
