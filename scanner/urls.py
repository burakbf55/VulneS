from django.urls import path
from . import views

urlpatterns = [
    path('', views.nmap_scanner, name='vulnerability_scanner')
]