from rest_framework import serializers
from .models import Candidatura
from .validators import validate_pdf, validate_file_size

class CandidaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = '__all__'  # ou liste explicitamente

    def validate_curriculo(self, file):
        validate_pdf(file)
        validate_file_size(file)
        return file

    def validate(self, data):
        if not data.get('aceita_lgpd'):
            raise serializers.ValidationError("É necessário aceitar a LGPD.")
        return data
