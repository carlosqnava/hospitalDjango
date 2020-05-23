from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Articulo, Venta, DetalleVenta
# from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from usuarios.models import Usuario
from django import template
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from hospital import settings
from django_weasyprint import WeasyTemplateResponseMixin


class Lista (ListView):
    model = Articulo
    paginate_by = 5

def comprar(request):
    pk = request.POST.get('id')
    cantidad = int(request.POST.get('cantidad'))
    

    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.stock > 0:
        # articulo.stock = articulo.stock - 1
        articulo.save()


        id = str(pk)

        request.session['total'] = request.session['total'] + float(articulo.precio)
        request.session['cuantos'] = request.session['cuantos'] + 1
        
        if id in request.session['articulos']:
            request.session['articulos'][id]['cantidad'] = request.session['articulos'][id]['cantidad'] + 1
        else: 
            request.session['articulos'][id] = {'nombre':articulo.nombre,'precio':float(articulo.precio),'cantidad': cantidad,}
    

            print(request.session['articulos'])


    return redirect('articulos:lista')

class VerCarrito(LoginRequiredMixin,ListView):
    model = Articulo
    template_name = 'articulos/venta_list.html'

    def get_queryset(self):

        id_articulos = list(self.request.session['articulos'].keys())

        carrito = list()

        for id in id_articulos:
            articulo = Articulo.objects.get(pk = id)
            cantidad = self.request.session['articulos'][id]['cantidad']

            tempo = (articulo,cantidad)
            print(tempo)

            carrito.append(tempo)


        return carrito

def confirmaCompra(request, pk):

    id_articulos = list(request.session.get('articulos').keys())

    print(id_articulos)
    print(Usuario.objects.get( pk = pk))

    venta = Venta.objects.create(fecha = datetime.now() , usuario = Usuario.objects.get( pk = pk))
    venta.save()


    for id in id_articulos:

        articulo = Articulo.objects.get(pk = id)
        cantidad = request.session['articulos'][id]['cantidad']
        articulo.stock = articulo.stock - cantidad
        articulo.save()

        detalle = DetalleVenta.objects.create(articulo = articulo, venta = venta)

        detalle.save()

    request.session['articulos'] = {}
    request.session['total'] = 0
    request.session['cuantos'] = 0  


    return redirect('articulos:lista')


def cancelarCompra(request):

    request.session['articulos'] = {}
    request.session['total'] = 0
    request.session['cuantos'] = 0  

    messages.error(request, 'Tu compra ha sido cancelada')

    return redirect('articulos:lista')


class VistaPdf(LoginRequiredMixin,ListView):
    model = DetalleVenta
    template_name = 'articulos/historial_pdf.html'

class HistorialVentasPdf(WeasyTemplateResponseMixin, VistaPdf):
    passpdf_stylesheets = [
        settings.STATICFILES_DIRS[0] + 'dist/css/adminlte.min.css',
    ]
    pdf_attachment = False
    pdf_filename = 'ventas.pdf'