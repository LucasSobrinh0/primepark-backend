import django_filters
from .models import Candidatura

class CandidaturaFilter(django_filters.FilterSet):
    # Campos do próprio modelo Candidatura
    cidade = django_filters.CharFilter(lookup_expr='icontains')
    bairro = django_filters.CharFilter(lookup_expr='icontains')
    uf = django_filters.CharFilter(lookup_expr='exact')
    escolaridade = django_filters.CharFilter(lookup_expr='exact')
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains')

    # Filtros relacionados (JOIN com Application)
    vaga = django_filters.NumberFilter(
        field_name='applications__vaga', lookup_expr='exact'
    )
    status = django_filters.CharFilter(
        field_name='applications__status', lookup_expr='exact'
    )

    class Meta:
        model = Candidatura
        # Em Meta.fields, inclua somente os campos que existem DE FATO no model Candidatura
        fields = {
            'nome': ['icontains'],
            'cidade': ['icontains'],
            'bairro': ['icontains'],
            'uf': ['exact'],
            'escolaridade': ['exact'],
        }

    # Para remover duplicidade caso haja múltiplas Applications por candidato
    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.distinct()
