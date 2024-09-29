from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    Tipos = [
        ('freelancer', 'Freelancer'),
        ('empresa', 'Empresa'),
    ]
    
    tipo_usuario = models.CharField(max_length=10, choices=Tipos)

    def __str__(self):
        return self.username 

class Freelancer(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='freelancer')
    nome = models.CharField(max_length=150)  
    cpf = models.CharField(max_length=11, unique=True) 
    email = models.EmailField(unique=True)  
    github = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='empresa')
    nome_empresa = models.CharField(max_length=150)  
    cnpj = models.CharField(max_length=14, unique=True)  
    email = models.EmailField(unique=True)  

    def __str__(self):
        return self.nome_empresa
