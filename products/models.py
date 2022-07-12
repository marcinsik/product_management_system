from django.db import models

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


