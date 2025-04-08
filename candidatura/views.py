from rest_framework import generics
from .models import Candidatura
from .serializers import CandidaturaSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from .filters import CandidaturaFilter
from django_filters.rest_framework import DjangoFilterBackend

class CandidaturaCreateAPIView(generics.CreateAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    permission_classes = [AllowAny]  # público


class CandidaturaListAPIView(generics.ListAPIView):
    queryset = Candidatura.objects.all().order_by('-criado_em')  # Exemplo: mais recentes primeiro
    serializer_class = CandidaturaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CandidaturaFilter
    # permission_classes = [IsAdminUser]  # Admin

class CandidaturaDetailAPIView(generics.RetrieveAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    # permission_classes = [IsAdminUser]  # Admin


class CandidaturaUpdateAPIView(generics.UpdateAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    # permission_classes = [IsAdminUser]  # Admin


class CandidaturaDestroyAPIView(generics.DestroyAPIView):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer
    # permission_classes = [IsAdminUser]  # Admin