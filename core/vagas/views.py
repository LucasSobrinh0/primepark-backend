from django.shortcuts import render
from rest_framework import generics
from .models import Application, Vaga
from .serializers import ApplicationSerializer, VagaSerializer
from rest_framework.permissions import AllowAny


class ApplicationCreateAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]

class ApplicationUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]


class VagaListCreateAPIView(generics.ListCreateAPIView):
    queryset = queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        # Verifica se já existe uma vaga com o título "Nenhuma"
        if not Vaga.objects.filter(titulo="Nenhuma").exists():
            Vaga.objects.create(titulo="Nenhuma", descricao="Vaga padrão")
        return Vaga.objects.all()


class VagaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [AllowAny]

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Application, Candidatura

class DashboardAPIView(APIView):
    def get(self, request):
        # Exemplo 1: total de candidatos por vaga
        candidatos_por_vaga = (
            Application.objects.values('vaga__titulo')
            .annotate(total=Count('candidatura'))
        )

        # Exemplo 2: candidatos por UF
        candidatos_por_uf = (
            Candidatura.objects.values('uf')
            .annotate(total=Count('id'))
        )

        # Exemplo 3: status de processos
        status_counts = (
            Application.objects.values('status')
            .annotate(total=Count('id'))
        )

        data = {
            "candidatos_por_vaga": list(candidatos_por_vaga),
            "candidatos_por_uf": list(candidatos_por_uf),
            "status_counts": list(status_counts),
        }
        return Response(data)


class ApplicationListAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]