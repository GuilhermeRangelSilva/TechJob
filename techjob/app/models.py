from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    tipo_usuario_choices = [
        ('freelancer', 'Freelancer'),
        ('empresa', 'Empresa'),
    ]
    
    tipo_usuario = models.CharField(
        max_length=10,
        choices=tipo_usuario_choices,
        default='freelancer',
    )

    def is_freelancer(self):
        return self.tipo_usuario == 'freelancer'
    
    def is_empresa(self):
        return self.tipo_usuario == 'empresa'


class Freelancer(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='freelancer_profile')
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email_freelancer = models.EmailField()
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='empresa_profile')
    nome_empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    email_empresa = models.EmailField()

    def __str__(self):
        return self.nome_empresa
