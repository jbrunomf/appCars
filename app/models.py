from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=120)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=7, unique=True, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='cars')
    photo = models.ImageField(upload_to='cars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    id = models.AutoField(primary_key=True)
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Qtd de Veículos: {self.cars_count} - Valor Total: {self.cars_value}'
