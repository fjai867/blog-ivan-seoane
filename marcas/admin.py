from django.contrib import admin

# Register your models here.
from .models import Marcas

# Register your models here.
class marcaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(Marcas,marcaAdmin)

