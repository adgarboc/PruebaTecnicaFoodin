from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=70)
    precio = models.DecimalField(max_digits=10, decimal_places=3)


