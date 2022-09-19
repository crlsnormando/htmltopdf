from django.shortcuts import render
from django.views.generic import ListView, View

from core.models import Funcionario
from core.report import GerarPdfMixin


from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
import io
from django.views import View
from django.views.generic import TemplateView



class FuncionariosListView(ListView):
    model = Funcionario
    template_name = 'listafuncionarios.html'
    context_object_name = 'funcionarios'  






class Pdf(View,GerarPdfMixin):
    def get(self, request):
        objects = Funcionario.objects.all()

        params = {
            "today": "variavel today",
            "sales": "Variavel sales",
            "request": request,
            "funcionarios": objects,
        }
        pdf= GerarPdfMixin()
        return self.render_pdf("funcionariospdf.html", params, "myfile")