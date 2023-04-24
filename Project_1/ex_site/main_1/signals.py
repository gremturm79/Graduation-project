from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
