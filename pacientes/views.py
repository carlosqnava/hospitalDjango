from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm
from django.urls import reverse_lazy


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
