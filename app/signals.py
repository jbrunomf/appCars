from django.db.models import Sum
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

from app.models import Car, CarInventory


@receiver(pre_save, sender=Car)
def pre_save_receiver(sender, instance, *args, **kwargs):
    print("pre_save_receiver")
    print(instance)


@receiver(post_save, sender=Car)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    print("post_save_receiver")
    update_inventory()


@receiver(pre_delete, sender=Car)
def pre_delete_receiver(sender, instance, *args, **kwargs):
    print("pre_save_receiver")
    print(pre_update_inventory())


@receiver(post_delete, sender=Car)
def post_delete_receiver(sender, instance, *args, **kwargs):
    update_inventory()
    print("post_delete_receiver")


def update_inventory():
    cars = Car.objects.all()
    car_inventory = CarInventory()
    car_inventory.cars_count = cars.count()
    car_inventory.cars_value = cars.aggregate(Sum('value'))['value__sum'] or 0
    car_inventory.save()


def pre_update_inventory():
    cars = Car.objects.all()
    cars_count = cars.count()
    cars_value = cars.aggregate(Sum('value'))
    return f'Total de veículos: {cars_count} - Valor total: R$ {cars_value}'
