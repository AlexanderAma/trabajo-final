from django.urls import path
from . import views

urlpatterns = [
    path("", views.saludar, name=""),
    path("peliculas/", views.listar_peliculas, name="peliculas"),
    path("series/", views.listar_series, name="series"),
    path("estrenos/", views.listar_estrenos, name="estrenos"),
    path("about/", views.about, name="about"),
    path("crear-serie/", views.crear_serie, name="crear_serie"),
    path("crear-pelicula/", views.crear_pelicula, name="crear_pelicula"),
    path("crear-estreno/", views.crear_estreno, name="crear_estreno"),
    path("buscar-pelicula/", views.buscar_pelicula, name="buscar_pelicula"),
]