from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import Paciente, Municipio, Estado
from .forms import PacienteForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
import datetime
from hospital import settings

from django.views.generic import DetailView


class Lista(ListView):
    model = Paciente


class Nuevo(CreateView):
    model = Paciente
    form_class = PacienteForm
    
    success_url = reverse_lazy('pacientes:lista')

class Editar(UpdateView):
    model = Paciente
    form_class = PacienteForm
    extra_context = {'editar':True}

    success_url = reverse_lazy('pacientes:lista')

class Eliminar(DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes:lista')


def buscar_municipio(request):
    id_estado = request.POST.get('id',None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id':mun.id,'nombre':mun.nombre} for mun in  municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'Parámetro inválido'}, safe=False)

class Grafica(TemplateView):
    template_name = 'pacientes/grafica.html'
    
    pacientes_tipo_sangre = Paciente.objects.all().values('tipo_sangre').annotate(cuantos=Count('tipo_sangre'))
    tipo_san = ['A+', 'A-', 'O+']

    datos = []
    for tipo in tipo_san:
        cuantos = 0
        for tp in pacientes_tipo_sangre:
            if tp['tipo_sangre'] == tipo:
                cuantos = tp['cuantos']
                break
        datos.append({'name':tipo, 'data':[cuantos]})

    extra_context = {'datos': datos}

class GraficaEdad(TemplateView):
    template_name = 'pacientes/grafica_edad.html'
    pacientes_fechas = Paciente.objects.all().values('fecha_nac').annotate(cuantos=Count('fecha_nac'))
    now = datetime.date.today()
    edades = []
    datos=[]

    for fechas in pacientes_fechas:
        diferencia = now - fechas['fecha_nac']
        anios = (int(diferencia.days / 365))
        edades.append(anios)

    #extra_context = {'datos': fechas['fecha_nac'], 'dat': anios}

    for edad in edades:
        cuantos = 0
        for ed in pacientes_fechas:
            diferencia = now - ed['fecha_nac']
            anios = (int(diferencia.days / 365))
            if anios == edad:
                cuantos = ed['cuantos']
                break
        datos.append({'data':[cuantos], 'name':edad})
        extra_context = {'datos':datos}

class VistaPdf(ListView):
    model = Paciente
    template_name = 'pacientes/pacientes_pdf.html'

class ListaPdf(WeasyTemplateResponseMixin, VistaPdf):
    passpdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'dist/css/adminlte.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'pacientes.pdf'

class VistaPacientePdf(DetailView):
    model = Paciente
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    template_name = 'pacientes/paciente_pdf.html'

class PacientePdf(WeasyTemplateResponseMixin, VistaPacientePdf):
    passpdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'dist/css/adminlte.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'paciente.pdf'

