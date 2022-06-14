from django.db import models
from requests import delete

# Create your models here.

class Equipo(models.Model):

    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=3)  
    username = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s - " % (self.nombre, 
                self.siglas,
                self.username)


class Jugador(models.Model):

    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    dorsal = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(Equipo, related_name='losjugadores', 
        on_delete = models.CASCADE)


    def __str__(self):
        return "%s - %s - %d - %d - %s" % (self.nombre,
                self.posicion,
                self.dorsal,
                self.sueldo,
                self.equipo.nombre)


class Campeonato(models.Model):
    campeonato = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - " % (self.campeonato, 
                self.auspiciante)

class CampeonatoEquipos(models.Model):
    """
    """
    anio = models.DateField()
    equipo = models.ForeignKey(Equipo, related_name='losequipos',
        on_delete = models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='loscampeonatos',
        on_delete = models.CASCADE)

    def __str__(self):
        return "%s - %s - %s - " % (self.anio, 
                self.equipo,
                self.campeonato)
    
