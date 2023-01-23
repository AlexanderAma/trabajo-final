from django import forms

class Peliculaformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)
    fecha_estreno = forms.DateField()

class Serieformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)
    plataforma= forms.CharField()


class Estrenosformulario(forms.Form):
    nombre_de_pelicula = forms.CharField(max_length=200)
    director = forms.CharField(max_length=200)
    pais_de_origen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500)

