from django.contrib import admin

# Register your models here.
from futbolec.models import *

admin.site.register(Equipo)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'dorsal', 'sueldo', 'equipo')
    search_fields = ('nombre', 'siglas')

admin.site.register(Jugador, JugadorAdmin)

admin.site.register(Campeonato)

class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display =  ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo', 'campeonato')
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)


