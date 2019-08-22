app_name = 'nome_aplicacao'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^novo-usuario/$', views.add_user, name='add_user'),
]
