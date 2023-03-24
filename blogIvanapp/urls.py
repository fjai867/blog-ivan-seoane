from django.urls import path
from blogIvanapp import views

urlpatterns = [
    
    path('',views.Inicio, name='Inicio'),
    path('Fotos/',views.Fotos, name='Fotos'),
    path('Videos/',views.Videos, name='Videos'),
    path('Marcas/',views.Marcas, name='Marcas'),
    path('Contacto/',views.Fotos, name='Contacto'),

    
]
