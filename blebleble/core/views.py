from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blebleble.tarefas.models import Tarefa

def home(request):
    tarefas = Tarefa.objects.all()
    return render(request,'core/index.html', {'tarefas': tarefas})
