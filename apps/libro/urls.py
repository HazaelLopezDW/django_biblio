from django.urls import path
from .views import *

urlpatterns = [
    path('crear_autor/', CrearAutor, name = 'crear_autor'),
    path('listar_autor/', ListadoAutor.as_view(), name = 'listar_autor'),
    path('editar_autor/<int:id>', EditarAutor, name = 'editar_autor'),
    path('eliminar_autor/<int:id>', EliminarAutor, name = 'eliminar_autor')
]
