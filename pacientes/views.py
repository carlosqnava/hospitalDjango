from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Paciente


class Lista(ListView):
    model = Paciente
