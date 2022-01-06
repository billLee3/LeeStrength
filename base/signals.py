from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.dispatch import receiver

# Need to connect the user form to have the email prefill the Profile Model. 
@receiver(post_save, sender=User)
def profileCreated(sender, instance, created, **kwargs):
    print("Signal Fired Profile Created")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username, 
            email = user.email,
        )
        
@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()

    
