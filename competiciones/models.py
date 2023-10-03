from django.db import models

# Create your models here.
class Campeonatos(models.Model):

    campeonato=models.CharField(max_length=60)
    poblacion=models.CharField(max_length=12)
    fecha=models.DateField()
    prueba=models.CharField(max_length=25)
    puesto=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)

    class Meta:
        verbose_name='competicion'
        verbose_name_plural='competiciones'

    def __str__(self):
        return self.campeonato