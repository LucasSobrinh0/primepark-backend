from django.db import models

class Regiao(models.Model):
    estado = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    cidade = models.CharField(max_length=255)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    escolaridade = models.CharField(max_length=255)
    experiencia = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"



    


class AnexoCurriculo(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='curriculos/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

