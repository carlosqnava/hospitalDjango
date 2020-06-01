from django.db import models
from django.utils.translation import ugettext_lazy as gettext


class Estado(models.Model):
    nombre = models.CharField('Nombre del estado',max_length=120)
    def __str__(self):
        return self.nombre
    

class Municipio(models.Model):
    nombre = models.CharField('Nombre del municipio',max_length=120)
    estado = models.ForeignKey(Estado, verbose_name="Estado", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    TIPO_SANGRE =  [
        ('A+', 'A +'),
        ('A-', 'A -'),
        ('O+', 'O +'),
    ]
    nombre = models.CharField(gettext("Nombre"),max_length=60)
    primerApellido = models.CharField(gettext("Apellido paterno"),max_length=60)
    segundoApellido = models.CharField(gettext("Apellido materno"), max_length=60, null=True, blank=True)
    numero_ss = models.CharField(gettext("Número de Seguro Social"),max_length=20)
    fecha_nac = models.DateField(gettext("Fecha de nacimiento"))
    tipo_sangre = models.CharField(gettext("Tipo de sangre"), max_length=3, choices=TIPO_SANGRE)
    municipio = models.ForeignKey(Municipio, verbose_name=gettext("Municipio"), on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, verbose_name=gettext("Estado"), on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nombre + ' ' + self.primerApellido
    