from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/' , include('pacientes.urls')),
    path('usuarios/' , include('usuarios.urls')),
    path('articulos/' , include('articulos.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
