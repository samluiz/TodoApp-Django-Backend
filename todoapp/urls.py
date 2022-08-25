from django.urls import path, include
from .views import taskApi

urlpatterns = [
  path('tasks/', taskApi),
]