from rest_framework import serializers
from . import models

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Points
        fields = "__all__"