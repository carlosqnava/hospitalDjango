from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Paciente
from .forms import PacienteForm


class Lista(ListView):
    model = Paciente


class Nuevo(CreateView):
    model = Paciente
    form_class = PacienteForm
