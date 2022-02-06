import re
from django.contrib.auth.models import User
from . import models
from rest_framework import serializers
from classification.serializers import PointSerializer

# Location of the user
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('x', 'y')

class RegisterSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False)
    points = PointSerializer(required=False)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password1 = self.validated_data['password']
        
        acc = User(username=self.validated_data['username'])
        acc.set_password(password1)
        acc.save()

        # Location need to be saved when user is created
        if self.validated_data['location']:
            loc = models.Location.objects.create(user=acc, **self.validated_data['location'])
            loc.user = acc
            loc.save()

        return acc