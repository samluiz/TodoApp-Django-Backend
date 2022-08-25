from django.urls import path, re_path
from .views import taskApi

urlpatterns = [
  re_path(r'^tasks/$', taskApi),
  re_path(r'^tasks/([0-9]+)$', taskApi)
]