from django.urls import path
from . import views

urlpatterns = [
    
    
    path('Competiciones/',views.listaEventos.as_view(), name='Competiciones'),
    
    
]