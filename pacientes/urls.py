from django.urls import path
from .views import Lista, Nuevo

app_name = 'pacientes'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('nuevo/', Nuevo.as_view(), name='nuevo'),
]
