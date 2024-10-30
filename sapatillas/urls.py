"""
URL configuration for sapatillas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from producto import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('marcas/', views.MarcaListView.as_view(), name='marca-list'),
    path('marcas/<int:pk>/', views.MarcaDetailView.as_view(), name='marca-detail'),
    path('marcas/nueva/', views.MarcaCreate.as_view(), name='marca-create'),
    path('marcas/<int:pk>/editar/', views.MarcaUpdate.as_view(), name='marca-update'),
    path('marcas/<int:pk>/eliminar/', views.MarcaDelete.as_view(), name='marca-delete'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categorias/nueva/', views.CategoriaCreate.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdate.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDelete.as_view(), name='categoria-delete'),
    
    path('zapatillas/', views.ZapatillaListView.as_view(), name='zapatilla-list'),
    path('zapatillas/nueva/', views.ZapatillaCreateView.as_view(), name='zapatilla-create'),
    path('zapatillas/<int:pk>/', views.ZapatillaDetailView.as_view(), name='zapatilla-detail'),
    path('zapatillas/<int:pk>/editar/', views.ZapatillaUpdateView.as_view(), name='zapatilla-update'),
    path('zapatillas/<int:pk>/eliminar/', views.ZapatillaDeleteView.as_view(), name='zapatilla-delete'),
]
