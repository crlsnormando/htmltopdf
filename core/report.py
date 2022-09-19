from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render



from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
import io
from django.views import View
from django.views.generic import TemplateView


class GerarPdfMixin:

    def render_pdf(self, path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type="application/pdf")
            response["Content-Disposition"] = "attachment;filename=%s.pdf" % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
