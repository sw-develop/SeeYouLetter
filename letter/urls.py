from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views
form letters import views

urlpatterns = [
    path('products/', views.ProductList.as_view())
    path('products/<int:pk>/', views.ProductDetail.as_view())
]