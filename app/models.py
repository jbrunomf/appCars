from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model



