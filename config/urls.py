from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('livros.html', LivrosView.as_view(), name='livros'),
    path('reserva.html', EmprestimoView.as_view(), name='reserva'),
    path('cidade.html', CidadesView.as_view(), name='cidade'),
    path('autor.html', AutoresView.as_view(), name='autor'),
    path('editora.html', EditorasView.as_view(), name='editora'),
    path('leitor.html', LeitoresView.as_view(), name='leitor'),
    path('genero.html', GenerosView.as_view(), name='genero'),
]