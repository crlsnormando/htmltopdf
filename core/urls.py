from .views import FuncionariosListView, Pdf
from django.urls import path

urlpatterns = [
    path('', FuncionariosListView.as_view()),
    path('relatoriopdf/', Pdf.as_view(), name='rlpdf'),
 
]
