from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.utils import timezone

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    today = timezone.now().date()
    return render(request, 'work10/todo_list.html', {'todos': todos, 'today': today})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('work10:todo_list')
    else:
        form = TodoForm()
    return render(request, 'work10/todo_form.html', {'form': form, 'mode': 'create'})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('work10:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'work10/todo_form.html', {'form': form, 'mode': 'edit', 'todo': todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('work10:todo_list')

@login_required
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('work10:todo_list')
