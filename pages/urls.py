from django.urls import path
from .views import home, about, calculator

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('calculator/',calculator, name='calculator'),
]