from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm, PerfilForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm


class Nuevo(CreateView):
    template_name = 'nuevo.html'
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')

class Perfil(SuccessMessageMixin, UpdateView):
    template_name = 'perfil.html'
    model = Usuario
    form_class = PerfilForm
    success_message = "El usuario %(first_name)s se actualizó con éxito"


    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        url = reverse_lazy('usuarios:perfil', kwargs={'pk': pk})
        return url