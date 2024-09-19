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
    value = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='cars')

    def __str__(self):
        return self.model
