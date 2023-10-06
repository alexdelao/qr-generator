
from django.urls import path
from .views import generate_qr, show_qr

urlpatterns = [
    path('', generate_qr, name='generate_qr'),
    path('show/<int:pk>/', show_qr, name='show_qr'),
]
