from django.shortcuts import render

# Data que se envía a los templates desde la vista
GENEROS = [
    {
        'slug': 'accion',
        'nombre': 'Acción',
        'descripcion': 'Persecuciones, peleas y mucha adrenalina de principio a fin.',
        'peliculas': [
            {'nombre': 'Deadpool & Wolverine', 'edad': '+18', 'imagen': 'images/accion1.jpg'},
            {'nombre': 'Vengadores: Endgame', 'edad': '+14', 'imagen': 'images/accion2.jpg'},
        ],
    },
    {
        'slug': 'terror',
        'nombre': 'Terror',
        'descripcion': 'Historias para pasar un buen susto y no dormir tranquilo.',
        'peliculas': [
            {'nombre': 'Five Nights at Freddy\'s', 'edad': '+14', 'imagen': 'images/terror1.jpg'},
            {'nombre': 'Five Nights at Freddy\'s 2', 'edad': '+14', 'imagen': 'images/terror2.jpg'},
        ],
    },
]


def inicio(request):
    return render(request, 'inicio.html', {'generos': GENEROS})


def genero(request):
    # Una sola página con todos los géneros y sus películas
    # Lista plana con todas las películas para el carousel
    carrusel = [dict(p, genero=g['nombre']) for g in GENEROS for p in g['peliculas']]
    return render(request, 'genero.html', {'generos': GENEROS, 'carrusel': carrusel})
