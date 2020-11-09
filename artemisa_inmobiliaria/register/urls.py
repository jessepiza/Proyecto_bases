from django.urls import path, include
from .views import index

app_name = 'Register'
urlpatterns = [
    path('', index),
]