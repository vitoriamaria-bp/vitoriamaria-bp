from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('cliente', 'Cliente'),
        ('freelancer', 'Freelancer'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Projeto(models.Model):
    STATUS_CHOICES = (
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    orcamento = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Orçamento (R$)")
    prazo = models.DateField(verbose_name="Prazo de Entrega")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meus_projetos')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo