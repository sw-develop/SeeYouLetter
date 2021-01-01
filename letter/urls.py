from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('letters/', views.LetterList.as_view()),
    path('letters/<int:pk>/', views.LetterDetail.as_view()),
    path('topics/', views.TopicList.as_view()),
    path('topics/<int:pk>/', views.TopicDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)