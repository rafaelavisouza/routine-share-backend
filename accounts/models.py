

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Eu separo dados "extras" do usuário aqui, pra não mexer no User do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos do mock da tela
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # Foto de perfil (opcional)
    photo = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"