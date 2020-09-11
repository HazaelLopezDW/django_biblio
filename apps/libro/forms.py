from django import forms
from .models import Autor

class AutorForm(forms.ModelsForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
