from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# --- TODO一覧 ---
def todo_list(request):
    sort = request.GET.get('sort', 'created_at')  # デフォルトは作成日
    show_incomplete = request.GET.get('incomplete', None)

    todos = Todo.objects.all().order_by(sort)
    if show_incomplete:
        todos = todos.filter(is_completed=False)

    return render(request, 'work09/todo_list.html', {'todos': todos})

# --- 新規作成 ---
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work09:todo_list')
    else:
        form = TodoForm()
    return render(request, 'work09/todo_form.html', {'form': form, 'mode': 'create'})

# --- 編集 ---
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('work09:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'work09/todo_form.html', {'form': form, 'mode': 'edit', 'todo': todo})

# --- 削除 ---
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('work09:todo_list')

# --- 完了/未完了 切り替え ---
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed   
    todo.save()
    return redirect('work09:todo_list')        
