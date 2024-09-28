from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('freelancer', 'Freelancer'),
        ('empresa', 'Empresa'),
    ]
    
    usuario = models.CharField(max_length=150, unique=True)  # Nome de usuário
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)  # Tipo de usuário

    def __str__(self):
        return self.usuario

class Freelancer(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='freelancer')
    nome = models.CharField(max_length=150)  # Nome do freelancer
    cpf = models.CharField(max_length=11, unique=True)  # CPF
    email = models.EmailField(unique=True)  # E-mail
    github = models.URLField(blank=True, null=True)  # GitHub

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='empresa')
    nome_empresa = models.CharField(max_length=150)  # Nome da empresa
    cnpj = models.CharField(max_length=14, unique=True)  # CNPJ
    email = models.EmailField(unique=True)  # E-mail da empresa

    def __str__(self):
        return self.nome_empresa
