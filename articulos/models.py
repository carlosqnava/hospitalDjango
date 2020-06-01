from django.db import models
from django.utils.translation import ugettext_lazy as gettext

# Create your models here.
class Articulo(models.Model):
    clave =  models.CharField(gettext("Clave"), max_length=30)
    nombre = models.CharField(gettext("Artículo"), max_length=150)
    descripcion =  models.CharField(gettext("Descripción"), max_length=300)
    imagen = models.ImageField(gettext("Imágen"), upload_to="articulos")
    precio =  models.DecimalField(gettext("Precio unitario"), max_digits=8, decimal_places=2)
    stock = models.IntegerField(gettext("Unidades"))
    categoria = models.ForeignKey("articulos.Categoria", verbose_name="Categoría", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(gettext("Categoría"), max_length=100)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name=gettext("Usuario"), on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fecha

class DetalleVenta(models.Model):
    articulo = models.ForeignKey("articulos.Articulo", verbose_name=gettext("Articulo"), on_delete=models.CASCADE)
    venta = models.ForeignKey("articulos.Venta", verbose_name=gettext("Venta"), on_delete=models.DO_NOTHING)

    def __str__(self):
        return '   || producto ||   '+self.articulo.nombre+'   || fecha  ||   '+self.venta.fecha.strftime('%d/%m/%Y')
