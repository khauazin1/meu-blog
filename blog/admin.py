from django.contrib import admin

from .models import Curso, InformacaoPessoal, Interesse

admin.site.register(Curso)
admin.site.register(Interesse)
admin.site.register(InformacaoPessoal)