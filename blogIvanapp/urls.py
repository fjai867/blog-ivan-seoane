from django.urls import path
from blogIvanapp import views


urlpatterns = [
    
    #path('',views.Inicio, name='Inicio'),
    
    path('Contacto/',views.Contacto, name='Contacto'),
    
]

