from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Paciente


class Lista(ListView):
    model = Paciente


class Nuevo(CreateView):
    pass
