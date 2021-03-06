"""sistemabiblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from autor.Api import viewSets as autorViewsSets
from editora.Api import viewSets as editoraViewsSets
from livro.Api import viewSets as livroViewsSets

from livro import urls as livro_url
from biblioteca import urls as biblioteca_url

router = routers.DefaultRouter()
router.register(r'autor', autorViewsSets.AutoresViewsSet)
router.register(r'livro', livroViewsSets.LivroViewsSet)
router.register(r'editora',editoraViewsSets.EditorasViewsSet)

schema_view = get_swagger_view(title='Biblioteca')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view),
    path('livro/',include(livro_url)),
    path('biblioteca/', include(biblioteca_url)),
    path('', RedirectView.as_view(url='biblioteca/'))
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)

