from django.shortcuts import render
from models import Todo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse

from form import TodoForm



# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    pass

def todo_post(request, pk):
    pass

@login_required()
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=todo)
        if form.is_valid():
            todo = form.save()
            context = {'form': form}

            return redirect(reverse('todo_detail', kwargs={'pk':todo.pk}))

    return render(request, 'todo_post.html', {'form': form})
