from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grupos_criados')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome