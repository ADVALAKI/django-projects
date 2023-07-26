from django.urls import path
from . import views

urlpatterns = [
    path('product1/', views.get_product)
    ]