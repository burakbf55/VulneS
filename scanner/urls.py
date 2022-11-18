from django.urls import path

from . import views

urlpatterns = [
    path('', views.nmap_scanner, name='vulnerability_scanner'),
    path('detail/<int:id>', views.nmap_detail, name='scanner_detail')
]