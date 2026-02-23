from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    DIFICULDADE_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Média'),
        ('D', 'Difícil'),
    ]
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES, default='F')
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

class Goal(models.Model):
    TIPO_CHOICES = [
        ('S', 'Semanal'),
        ('M', 'Mensal'),
    ]
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='S')
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Meta: {self.titulo} - {self.usuario.username}"