from django.db import models
from .validators import validate_file_size, validate_pdf
import django_filters


ESTADOS_CHOICES = [
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('SP', 'São Paulo'),
    # Adicione outras UF se precisar
]

ESCOLARIDADE_CHOICES = [
    ('EMI', 'Ensino Médio Incompleto'),
    ('EMC', 'Ensino Médio Completo'),
    ('ESI', 'Ensino Superior Incompleto'),
    ('ESC', 'Ensino Superior Completo'),
    # Adicione mais se precisar
]

def upload_curriculo(instance, filename):
    # Opcionalmente, você pode personalizar o caminho onde o currículo é salvo
    # Exemplo: "curriculos/2025/04/<id_do_candidato>_<filename>"
    return f"curriculos/{instance.id or 'temp'}_{filename}"


class Candidatura(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    
    uf = models.CharField(
        max_length=2,
        choices=ESTADOS_CHOICES,
        verbose_name="Estado"
    )
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(
        max_length=100,
        blank=True,    # Permite ficar em branco
        null=True      # Permite valor nulo no banco
    )
    
    escolaridade = models.CharField(
        max_length=3,
        choices=ESCOLARIDADE_CHOICES,
        blank=True,
        null=True
    )
    
    # Limite de 300 caracteres
    sobre_voce = models.CharField(
        max_length=300,
        verbose_name="Fale sobre você"
    )
    
    # FileField para PDF até 5 MB; validações podem ser feitas no Serializer
    curriculo = models.FileField(
    upload_to=upload_curriculo,
    validators=[validate_pdf, validate_file_size],
    null=True,
    blank=True,
    verbose_name="Currículo (PDF até 5MB)"
)
    
    # Check de aceite da LGPD
    aceita_lgpd = models.BooleanField(default=False)
    
    # Auxilia para saber quando foi criado/atualizado
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nome} - {self.email}"

