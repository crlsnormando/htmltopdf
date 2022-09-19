from pyexpat import model
from sre_parse import Verbose
from tabnanny import verbose
from django.db import models

# Create your models here.
class Funcionario(models.Model):
    TIPOS_FUNC = (
        ('Contador', 'CONTADOR'),
        ('Administrador', 'ADMINISTRADOR'),
        ('Economista', 'ECONOMISTA'),
        ('Outros', 'OUTRO'),
    )
    nome = models.CharField('Nomes', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    funcao = models.CharField('Funções', max_length=13, choices=TIPOS_FUNC)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['-nome', 'sobrenome']
    
    def __str__(self):
        return self.nome +' '+ self.sobrenome