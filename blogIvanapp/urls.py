from django.urls import path
from blogIvanapp import views


urlpatterns = [
    
    #path('',views.Inicio, name='Inicio'),
    path('Eventos/',views.Eventos, name='Eventos'),
    path('Contacto/',views.Contacto, name='Contacto'),
    
]

