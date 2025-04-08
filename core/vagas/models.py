from django.db import models
from candidatura.models import Candidatura

# models.py (pode ser no mesmo app candidatura ou outro app, ex: vagas)
class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    criterios = models.JSONField(default=list, blank=True)  # Aqui armazenamos a lista de critérios
    # etc. Campos adicionais se quiser

    def __str__(self):
        return self.titulo


class Application(models.Model):
    candidatura = models.ForeignKey(Candidatura, on_delete=models.CASCADE, related_name="applications")
    vaga = models.ForeignKey(
        Vaga, 
        on_delete=models.CASCADE,
        related_name="applications",
        null=True,      # Permite valor nulo no DB
        blank=True,      # Permite ficar em branco nos formulários
        default='Nenhuma'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_planejada_inicio = models.DateField(blank=True, null=True)

    STATUS_CHOICES = [
        ('NAO_SELECIONADO', 'Não selecionado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONTRATADO', 'Contratado'),
        ('NAO_APTO', 'Não apto no momento'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM_ANDAMENTO')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidatura.nome} - {self.vaga.titulo}"
