

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relacionamento 1 para 1 com o usuário padrão do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)
    pontos_totais = models.IntegerField(default=0)
    
    # Usamos string 'groups_app.Group' para evitar erro de importação circular
    grupo_atual = models.ForeignKey('groups_app.Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username