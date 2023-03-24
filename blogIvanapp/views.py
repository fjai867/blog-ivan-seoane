from django.shortcuts import render,HttpResponse

# Create your views here.

def Inicio(request):
    return render(request, 'blogIvanapp/homme.html')

def Fotos(request):
    return HttpResponse('Fotos')

def Videos(request):
    return HttpResponse('Videos`')

def Marcas(request):
    return HttpResponse('Marcas')

def Contacto(request):
    return HttpResponse('Contacto')

