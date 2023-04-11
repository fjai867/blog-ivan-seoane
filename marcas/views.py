from django.shortcuts import render
from .models import Marcas
from django.views.generic import ListView

# Create your views here.
class listaMarcas(ListView):
    model=Marcas
    template_name="marcas/marcas.html"


