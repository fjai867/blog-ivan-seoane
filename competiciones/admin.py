from django.contrib import admin

# Register your models here.
from .models import Campeonatos


class competAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')



admin.site.register(Campeonatos,competAdmin)

