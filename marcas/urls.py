from django.urls import path
from . import views

urlpatterns = [
    
    
    path('Marcas/',views.listaMarcas.as_view(), name='Marcas'),
    
    
]