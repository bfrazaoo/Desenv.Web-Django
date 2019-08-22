from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa

# Create your views here.

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:nova_tarefa')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render (request, 'tarefas/lista_categoria.html', {'categorias': categorias})


def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core')
        else:
            print(form.errors)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

def delete_tarefa(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa).delete()
    return redirect('core')

def editar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = TarefaForm(request, POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(instance=tarefa)
    return render (request, 'tarefas/nova_tarefa.html', {'form': form})
