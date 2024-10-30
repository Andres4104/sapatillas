from django.db import models

#PRODUCTOS
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='marcas/')

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Zapatilla(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
<<<<<<< HEAD
    imagen = models.ImageField(upload_to='zapatillas/', blank=True, null=True)
=======
    imagen = models.ImageField(upload_to='zapatillas/', blank=False, null=False)
>>>>>>> 3a3509f (Primer commit: inicia el repositorio de sapatillas)

    def __str__(self):
        return self.nombre
