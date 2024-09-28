from django.db import models

class Usuario(models.Model):
    Tipos = [
        ('freelancer', 'Freelancer'),
        ('empresa', 'Empresa'),
    ]
    
    usuario = models.CharField(max_length=150, unique=True)  
    tipo_usuario = models.CharField(max_length=10, choices=Tipos)  

    def __str__(self):
        return self.usuario

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
