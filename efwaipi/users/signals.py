from django.db.models.signals import post_save
from django.contrib.auth.models import User #sending the signal
from django.dispatch import receiver # receive signal and do some tasks
from .models import Profile

# when user is saved, signal is sent, receive by receiver, create profile, takes all args ^instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #kwargs accept any additional keywords
    instance.profile.save()