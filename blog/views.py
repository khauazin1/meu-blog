from django.shortcuts import render

from .models import Curso, InformacaoPessoal, Interesse


def home(request):
    info_pessoal = InformacaoPessoal.objects.first()
    return render(request, 'home.html', {'info_pessoal': info_pessoal})

def sobre(request):
    return render(request, 'sobre.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def interesses(request):
    interesses = Interesse.objects.all()
    return render(request, 'interesses.html', {'interesses': interesses})
