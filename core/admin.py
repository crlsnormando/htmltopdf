
from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display =('nomecompleto', 'funcao')

    def nomecompleto(self, func):
        return str(func)