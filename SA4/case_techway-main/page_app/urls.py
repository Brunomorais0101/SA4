from django.urls import path
from .views import index, contato, services  # Adicione 'services' à lista de imports

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('services/', services, name='services'),  # Adicione esta linha
]
