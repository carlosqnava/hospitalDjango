from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    rfc = models.CharField('R.F.C.', max_length=13)
    foto = models.ImageField('Foto', upload_to='perfil', blank=True, null=True)

    def __str__(self):
        return self.username
    
class Grupo(models.Model):
    grupo = models.CharField('Nombre del Grupo', max_length=120, null=False)
    def __str__(self):
        return self.grupo
        
