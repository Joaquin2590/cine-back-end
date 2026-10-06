from django.http import Http404
from django.shortcuts import render

# Data que se envía a los templates desde la vista
GENEROS = [
    {
        'slug': 'accion',
        'nombre': 'Acción',
        'descripcion': 'Persecuciones, peleas y mucha adrenalina de principio a fin.',
        'peliculas': [
            {'nombre': 'Mad Max: Furia en el camino', 'edad': '+14', 'imagen': 'images/madmax.jpg'},
            {'nombre': 'John Wick', 'edad': '+18', 'imagen': 'images/johnwick.jpg'},
        ],
    },
    {
        'slug': 'terror',
        'nombre': 'Terror',
        'descripcion': 'Historias para pasar un buen susto y no dormir tranquilo.',
        'peliculas': [
            {'nombre': 'El Conjuro', 'edad': '+14', 'imagen': 'images/conjuro.jpg'},
            {'nombre': 'It (Eso)', 'edad': '+16', 'imagen': 'images/it.jpg'},
        ],
    },
]


def inicio(request):
    return render(request, 'inicio.html', {'generos': GENEROS})


def genero(request, slug):
    for g in GENEROS:
        if g['slug'] == slug:
            return render(request, 'genero.html', {'genero': g})
    raise Http404('Género no encontrado')
