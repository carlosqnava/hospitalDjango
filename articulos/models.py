from django.db import models

# Create your models here.
class Articulo(models.Model):
    clave =  models.CharField("Clave", max_length=30)
    nombre = models.CharField("Artículo", max_length=150)
    descripcion =  models.CharField("Descripción", max_length=300)
    imagen = models.ImageField("Imágen", upload_to="articulos")
    precio =  models.DecimalField("Precio unitario", max_digits=8, decimal_places=2)
    stock = models.IntegerField("Unidades")
    categoria = models.ForeignKey("articulos.Categoria", verbose_name="Categoría", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField("Categoría", max_length=100)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name="Usuario", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fecha

class DetalleVenta(models.Model):
    articulo = models.ForeignKey("articulos.Articulo", verbose_name="Articulo", on_delete=models.CASCADE)
    venta = models.ForeignKey("articulos.Venta", verbose_name="Venta", on_delete=models.DO_NOTHING)

    def __str__(self):
        return '   || producto ||   '+self.articulo.nombre+'   || fecha  ||   '+self.venta.fecha.strftime('%d/%m/%Y')
