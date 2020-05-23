from django.urls import path
from .views import Lista, comprar,  confirmaCompra, cancelarCompra, VerCarrito, HistorialVentasPdf



app_name = 'articulos'

urlpatterns = [
    path('lista/', Lista.as_view(), name='lista'),
    path('comprar/', comprar, name='comprar'),
    path('vercarrito/',VerCarrito.as_view(),name='vercarrito'),
    path('confirmaCompra/<int:pk>',confirmaCompra,name='confirmaCompra'),
    path('cancelarCompra/',cancelarCompra, name='cancelarCompra'),
    path('historial_pdf/', HistorialVentasPdf.as_view(), name='historial'),
   
]
