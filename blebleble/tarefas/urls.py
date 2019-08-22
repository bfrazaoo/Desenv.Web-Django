app_name = 'nome_aplicacao'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^nova-categoria/$',views.nova_categoria, name='nova_categoria'),
    url(r'^nova-tarefa/$',views.nova_tarefa, name='nova_tarefa'),
    url(r'^editar-tarefa/(?P<id_tarefa>[0-9]+)/$',views.editar_tarefa, name= 'editar_tarefa'),
    url(r'^delete-tarefa/(?P<id_tarefa>[0-9]+)/$',views.delete_tarefa, name='delete_tarefa'),
]
