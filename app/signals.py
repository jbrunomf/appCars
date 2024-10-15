from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

from app.models import Car


@receiver(pre_save, sender=Car)
def pre_save_receiver(sender, instance, *args, **kwargs):
    print("pre_save_receiver")
    print(instance)

@receiver(post_save, sender=Car)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    print("post_save_receiver")
    print(instance)


@receiver(pre_delete, sender=Car)
def pre_delete_receiver(sender, instance, created, *args, **kwargs):
    print("post_save_receiver")
    print(instance)


@receiver(post_delete, sender=Car)
def post_delete_receiver(sender, instance, created, *args, **kwargs):
    print("post_save_receiver")
    print(instance)
