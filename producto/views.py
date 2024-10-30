from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Marca, Categoria , Zapatilla
from django.urls import  reverse_lazy
# Create your views here.

class MarcaDetailView(DetailView):
    model = Marca

class CategoriaDetailView(DetailView):
    model = Categoria

class MarcaListView(ListView):
    model = Marca

class CategoriaListView(ListView):
    model = Categoria

class MarcaCreate(CreateView):
    model = Marca
    fields = '__all__'
    success_url = reverse_lazy('marca-list')

class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('marca-list')

class MarcaUpdate(UpdateView):
    model = Marca
    fields = '__all__'

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = '__all__'

class MarcaDelete(DeleteView):
    model = Marca
    success_url = reverse_lazy('marca-list')

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria-list')
    
class ZapatillaListView(ListView):
    model = Zapatilla
    
class ZapatillaDetailView(DetailView):
    model = Zapatilla

class ZapatillaCreateView(CreateView):
    model = Zapatilla
    fields = '__all__'
    success_url = '/zapatillas/'

class ZapatillaUpdateView(UpdateView):
    model = Zapatilla
    fields = '__all__'

class ZapatillaDeleteView(DeleteView):
    model = Zapatilla
    success_url = reverse_lazy('zapatilla-list')