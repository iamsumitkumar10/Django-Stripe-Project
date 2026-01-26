from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-checkout/', views.create_checkout, name='checkout'),
    path('success/', views.payment_success, name='success'),
]
