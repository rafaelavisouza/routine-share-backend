from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Quando eu crio um User, eu já crio o Profile automaticamente
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Quando eu salvo User, eu garanto que o Profile existe e salva também
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Se por algum motivo o profile não existir, eu crio
    Profile.objects.get_or_create(user=instance)
    instance.profile.save()