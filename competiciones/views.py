from .models import Campeonatos
from django.views.generic import ListView

# Create your views here.
class listaEventos(ListView):
    models = Campeonatos
    queryset = Campeonatos.objects.all()
    template_name="eventos.html"
    context_object_name = 'campeonato'
