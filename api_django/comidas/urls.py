from django.urls import path
from .views import listar_comidas

urlpatterns = [
    path("comidas", listar_comidas),
]
