from django.urls import path, include
from .views import taskApi

urlpatterns = [
  path(r'^tasks/$', taskApi),
  path(r'^tasks/([0-9]+)$', taskApi)
]