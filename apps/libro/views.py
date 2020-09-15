from django.shortcuts import render,redirect

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return redirect(request,'libro/crear_autor.html', {'autor_form':autor_form})
