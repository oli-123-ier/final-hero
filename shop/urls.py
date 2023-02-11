from django.shortcuts import render

from django.urls import path
from shop.views import index, detail, checkout, Confirmation

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', Confirmation, name="confirmation"),
]
