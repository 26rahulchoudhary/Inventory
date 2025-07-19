from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # description = models.TextField(blank=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.sku})"
