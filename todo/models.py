from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    
    TOP= "TOP"
    LATE= "LTR"
    NO = "NO"

    TODO_PRIORITIE_CHOICES = [
        (TOP, "Top Priority"),
        (LATE, "Later Priority"),
        (NO, "Not a Priority")
    ]

    todo_priorities = models.CharField(
        max_length=3,
        choices = TODO_PRIORITIE_CHOICES,
        default = TOP,
    )

    title = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

        