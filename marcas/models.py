from django.db import models

# Create your models here.
class Marcas(models.Model):

    prueba=models.CharField(max_length=50)
    marca=models.CharField(max_length=12)
    agno=models.CharField(max_length=4)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'

    def __str__(self):
        return self.prueba