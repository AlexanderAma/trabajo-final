from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from critica_cine.forms import Peliculaformulario, Serieformulario, Estrenosformulario
from critica_cine.models import Peliculas, Series, Proximos_estrenos


# Create your views here.
def saludar(request):
     return render(
        request=request,
        template_name="critica_cine/saludar.html"
        )
    



def about(request):
    contexto= {"about": about}
    return render(
        request=request,
        template_name="critica_cine/about.html"
    )


def listar_peliculas(request):
    contexto = {
        "peliculas": Peliculas.objects.all()
    }
    return render(
        request=request, 
        template_name="critica_cine/lista_peliculas.html",
        context=contexto
        )

def listar_series(request):
    contexto = {
        "series":Series.objects.all()
    }
    return render(
        request=request,
         template_name="critica_cine/lista_series.html",
         context=contexto
         )


def listar_estrenos(request):
    contexto = {
        "estrenos":Proximos_estrenos.objects.all()
    }
    return render(
        request=request,
         template_name="critica_cine/lista_estrenos.html",
         context=contexto
         )

def crear_serie(request):
    if request.method == "POST":
        formulario = Serieformulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            serie = Series(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"], plataforma=data["plataforma"] )
            serie.save()
            url_exitosa = reverse("series")
            return redirect(url_exitosa)

    else:

        formulario = Serieformulario()
    return render(
            request=request,
            template_name="critica_cine/formulario_serie.html",
            context= {"formulario": formulario},
        )
    
def crear_pelicula(request):
    if request.method == "POST":
       formulario = Peliculaformulario(request.POST)
       if formulario.is_valid():
        data = formulario.cleaned_data
        pelicula = Peliculas(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"], fecha_estreno=data["fecha_estreno"] )
        pelicula.save()
        url_exitosa = reverse("peliculas")
        return redirect(url_exitosa)

    else:
        formulario =Peliculaformulario()
          
    return render(
            request=request,
            template_name="critica_cine/formulario_pelicula.html",
            context= {"formulario": formulario},
        )


def crear_estreno(request):
    if request.method == "POST":
       formulario = Estrenosformulario(request.POST)
       if formulario.is_valid():
        data = formulario.cleaned_data
        estreno = Proximos_estrenos(nombre_de_pelicula=data["nombre_de_pelicula"], descripcion=data["descripcion"], director=data["director"], pais_de_origen=data["pais_de_origen"] )
        estreno.save()
        url_exitosa = reverse("estrenos")
        return redirect(url_exitosa)

    else:
        formulario =Estrenosformulario()
          
    return render(
            request=request,
            template_name="critica_cine/formulario_estreno.html",
            context= {"formulario": formulario},
        )

def buscar_pelicula(request):
    if request.method == "POST":
       data = request.POST
       peliculas = Peliculas.objects.filter(nombre_de_pelicula__contains= data["nombre_de_pelicula"])
       contexto = {
              "peliculas": peliculas
       }
       return render(
             request=request,
             template_name= "critica_cine/lista_peliculas.html",
             context = contexto,
       )

    else:
        return render(
            request=request,
            template_name="critica_cine/busqueda_pelicula.html"

        )




