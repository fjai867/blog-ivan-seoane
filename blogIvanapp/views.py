from django.shortcuts import render,HttpResponse

# Create your views here.

def Inicio(request):
    return render(request, 'blogIvanapp/homme.html')



def Videos(request):
    return render(request, 'blogIvanapp/videos.html')

def Marcas(request):
    return render(request, 'blogIvanapp/marcas.html')

def Eventos(request):
    return render(request, 'blogIvanapp/eventos.html')

def Contacto(request):
    return render(request, 'blogIvanapp/contacto.html')

