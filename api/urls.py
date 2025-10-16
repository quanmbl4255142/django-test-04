from django.urls import path
from . import views

urlpatterns = [
    path('getcook/', views.cookListCreateView.as_view(), name='getcook-list'),
    path('getcook/<int:pk>/', views.cookDetailView.as_view(), name='getcook-detail'),
    path('health/', views.health_check, name='health-check'),
]
