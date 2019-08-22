from django.contrib import admin

# Register your models here.
from .models import Categoria, Tarefa

class CategoriaAdmin(admin.ModelAdmin):
    pass

class TarefaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria)
admin.site.register(Tarefa)
