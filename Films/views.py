from django.shortcuts import render
from .models import Films

# Create your views here.


def PaginaInicial(request):
    lista_filmes = Films.objects.all()

    return render(request, "index.html", {"listaFilms": lista_filmes})
