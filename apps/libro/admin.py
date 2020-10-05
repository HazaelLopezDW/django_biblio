from django.contrib import admin
from .models import Autor,Libro

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellidos']
    list_display = ('nombre', 'apellidos', 'nacionalidad', 'estado', 'fecha_creacion',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro)
