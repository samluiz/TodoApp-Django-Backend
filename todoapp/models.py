from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  taskId = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  complete = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title