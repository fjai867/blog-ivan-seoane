from django.db import models

# Create your models here.

class videos(models.Model):
    nombre = models.CharField(max_length=120)
    video=models.FileField(upload_to=('video/%y'))
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='video'
        verbose_name_plural='videos'
    
    def __str__(self):
        return self.nombre

