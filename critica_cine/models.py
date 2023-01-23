from django.db import models

# Create your models here.
class Peliculas(models.Model):
    nombre_de_pelicula = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    pais_de_origen = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fecha_estreno = models.DateField()

    def __str__(self):
        return f"{self.nombre_de_pelicula}. {self.director}. {self.pais_de_origen}. {self.descripcion}.{self.fecha_estreno}"

class Proximos_estrenos(models.Model):
    nombre_de_pelicula = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    pais_de_origen = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.nombre_de_pelicula}. {self.director}. {self.pais_de_origen}. {self.descripcion}"


class Series(models.Model):
    nombre_de_pelicula = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    pais_de_origen = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    plataforma = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre_de_pelicula}. {self.director}. {self.pais_de_origen}. {self.descripcion}.{self.plataforma}"



class Valoracion_cine(models.Model):
     nombre_de_pelicula = models.CharField(max_length=200)
     puntos = float()
     comentario = models.CharField(max_length=500)
     pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    
     def __str__(self):
        return f"{self.nombre_de_pelicula}. {self.puntos}. {self.comentario}. {self.pelicula}"



class Valoracion_serie(models.Model):
     nombre_de_pelicula = models.CharField(max_length=200)
     puntos = float()
     comentario = models.CharField(max_length=500)
     pelicula = models.ForeignKey(Series, on_delete=models.CASCADE)

     def __str__(self):
        return f"{self.nombre_de_pelicula}. {self.puntos}. {self.comentario}. {self.pelicula}"
