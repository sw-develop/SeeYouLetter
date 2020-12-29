from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('photos/', views.PhotoList.as_view()),
    path('photos/<int:pk>/', views.PhotoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)