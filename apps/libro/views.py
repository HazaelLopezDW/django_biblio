from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView,ListView

"""
    1.- dispach: Valida la peticion y elige que metodo HTTP se utlizo para la solicitud
    2.- http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    3.- options()
"""

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

def CrearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})



def ListarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autor.html',{'autores':autores})

def EditarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'libro/crear_autor.html', {'autor_form':autor_form, 'error':error})

def EliminarAutor(request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html',{'autor':autor})
