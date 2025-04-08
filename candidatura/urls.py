from django.urls import path
from .views import CandidaturaCreateAPIView, CandidaturaDestroyAPIView, CandidaturaListAPIView, CandidaturaUpdateAPIView, CandidaturaDetailAPIView

urlpatterns = [
    path('create/', CandidaturaCreateAPIView.as_view(), name='candidatura-create'),
    path('list/', CandidaturaListAPIView.as_view(), name="candidatura-list"),
    path('detail/<int:pk>/', CandidaturaDetailAPIView.as_view(), name="candidatura-detail"),
    path('update/<int:pk>/', CandidaturaUpdateAPIView.as_view(), name="candidatura-update"),
    path('delete/<int:pk>/', CandidaturaDestroyAPIView.as_view(), name="candidatura-delete")
]