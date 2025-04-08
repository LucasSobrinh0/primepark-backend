from rest_framework import serializers
from .models import Application, Vaga

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    vaga = serializers.PrimaryKeyRelatedField(
        queryset=Vaga.objects.all(),
        allow_null=True,        # Permite vaga nula
        required=False          # Não obriga enviar
    )

    class Meta:
        model = Application
        fields = '__all__'
