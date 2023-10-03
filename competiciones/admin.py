from django.contrib import admin

# Register your models here.
from competiciones.models import Campeonatos


#class competAdmin(admin.ModelAdmin):
    #readonly_fields = ('created','updated')


admin.site.register(Campeonatos)

