from django.urls import path
from . import views
from main.views import index, contacts, product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('product/<int:product_id>/', views.product, name='product'),
]




