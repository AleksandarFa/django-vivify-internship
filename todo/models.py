from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    TOP = "TOP"
    MID = "MID"
    LOW = "LOW"

    TODO_PRIORITY_CHOICES = [
        (TOP, "Top priority"),
        (MID, "Mid lvl priority"),
        (LOW, "Low lvl priority"),
    ]

    todo_priority = models.CharField(max_length=3, choices=TODO_PRIORITY_CHOICES, default=LOW)
