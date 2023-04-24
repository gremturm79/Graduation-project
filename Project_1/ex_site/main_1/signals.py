from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User


#@receiver(post_save, sender=User)
#def update_user(sender, instance, created, **kwargs):
    #custom = instance
    #user = custom.user
    #user.first_name = custom.name
    #user.username = custom.username
    #user.email = custom.email
    #print(user.first_name)
    #user.save()


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
