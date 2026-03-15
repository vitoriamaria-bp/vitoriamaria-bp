from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('cliente', 'Cliente'),
        ('freelancer', 'Freelancer'),
    )
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    cpf_cnpj = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username