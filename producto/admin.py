from django.contrib import admin
from .models import Marca, Zapatilla, Categoria

# Register your models here.

admin.site.register(Marca)
admin.site.register(Zapatilla)
admin.site.register(Categoria)

