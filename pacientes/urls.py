from django.urls import path
from .views import Lista, Nuevo, Eliminar, Editar, buscar_municipio, Grafica, GraficaEdad, ListaPdf, PacientePdf

app_name = 'pacientes'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('nuevo/', Nuevo.as_view(), name='nuevo'),
    path('editar/<int:pk>', Editar.as_view(), name='editar'),
    path('eliminar/<int:pk>', Eliminar.as_view(), name='eliminar'),
    path('busca-municipio/', buscar_municipio, name='buscar_municipio'),
    path('grafica/', Grafica.as_view(), name='grafica'),
    path('grafica_edad/', GraficaEdad.as_view(), name='grafica_edad'),

    path('pdf/', ListaPdf.as_view(), name='lista_pdf'),
    path('pdf-paciente/<int:pk>', PacientePdf.as_view(), name='paciente_pdf'),

]
