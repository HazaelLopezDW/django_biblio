from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    if request.method = 'POST':
        
