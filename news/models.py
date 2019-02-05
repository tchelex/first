from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ListOfStudents (models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    text = models.TextField()
    section = models.CharField(max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)   #дата которая не изменяется дата создания
    date = models.DateTimeField(default=timezone.now)       #дата которая изменяется изменений (или в ручную)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
