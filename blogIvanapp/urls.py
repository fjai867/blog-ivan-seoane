from django.urls import path
from blogIvanapp import views


urlpatterns = [
    
    path('',views.Inicio, name='Inicio'),
    path('Videos/',views.Videos, name='Videos'),
    path('Marcas/',views.Marcas, name='Marcas'),
    path('Eventos/',views.Eventos, name='Eventos'),
    path('Contacto/',views.Contacto, name='Contacto'),

    
]

