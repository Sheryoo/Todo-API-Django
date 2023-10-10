from django.db import models

# Create your models here.

class Todo (models.Model):
  task = models.CharField(max_length=100, blank=False)
  completed = models.BooleanField(default=False)
  date = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True)

  def __str__(self):
    return self.task
  