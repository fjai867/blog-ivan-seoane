from django.shortcuts import render
from .models import Marcas

# Create your views here.
def Marcas(request):
    return render(request, 'marcas/marcas.html')
