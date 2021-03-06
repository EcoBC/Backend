from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# User's Place of living
class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)