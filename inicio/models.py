from django.db import models

# Create your models here.

class Productos(models.Model):
    Producto = models.CharField(max_length=50)
    Descripcion = models.TextField()
    Precio = models.IntegerField()

    def __str__(self):
        return f'{self.Producto} {self.Descripcion} {self.Precio}'