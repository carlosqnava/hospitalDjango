from django.urls import path
from .views import Lista, Login, Nuevo, Perfil, ActivarCuenta
from django.contrib.auth.views import LogoutView



app_name = 'usuarios'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('nuevo/', Nuevo.as_view(), name='nuevo'),
    path('perfil/<int:pk>', Perfil.as_view(), name='perfil'),
    path('activar/<slug:uidb64>/<slug:token>', ActivarCuenta.as_view(), name='activar')
]
