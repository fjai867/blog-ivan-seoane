from django.db import models

# Create your models here.
class Campeonatos(models.Model):

    campeonato=models.CharField(max_length=60)
    poblacion=models.CharField(max_length=12)
    fecha=models.DateField(auto_now_add=True)
    puesto=models.CharField(max_length=6)
    marca=models.DateTimeField(max_length=10)

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'

    def __str__(self):
        return self.campeonato