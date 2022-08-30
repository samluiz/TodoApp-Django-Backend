from django.urls import path, re_path
from .views import taskApi, taskApiFiltered

urlpatterns = [
  path('tasks/', taskApi, name="tasks"),
  path('tasks/<int:id>', taskApiFiltered, name="taskId")
]