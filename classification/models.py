from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User's points for recycling
class Points(models.Model):
    score = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='points')