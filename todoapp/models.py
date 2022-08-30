from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  title = models.CharField(max_length=200, blank=True)
  description = models.TextField(null=True, blank=True)
  complete = models.BooleanField(default=False, blank=True)
  created = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return self.title