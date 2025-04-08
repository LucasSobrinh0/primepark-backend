# vagas/urls.py
from django.urls import path
from .views import (
    ApplicationCreateAPIView, 
    ApplicationUpdateAPIView, 
    DashboardAPIView,
    VagaListCreateAPIView,
    VagaRetrieveUpdateDestroyAPIView,
    ApplicationListAPIView
)

urlpatterns = [
    path('application/', ApplicationListAPIView.as_view(), name='application-list'),
    path('application/create/', ApplicationCreateAPIView.as_view(), name='application-create'),
    path('application/update/<int:pk>/', ApplicationUpdateAPIView.as_view(), name='application-update'),
    path('vaga/', VagaListCreateAPIView.as_view(), name='vaga-list-create'),
    path('vaga/<int:pk>/', VagaRetrieveUpdateDestroyAPIView.as_view(), name='vaga-rud'),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
]