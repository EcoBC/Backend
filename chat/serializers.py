from attr import field
from django.contrib.auth.models import User
from typer import style
from . import models
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('x', 'y')

class RegisterSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False)

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

        if self.validated_data['location']:
            loc = models.Location.objects.create(user=acc, **self.validated_data['location'])
            loc.user = acc
            loc.save()

        return acc