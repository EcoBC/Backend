from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from . import predict, models
import os
import tensorflow as tf
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Create your views here.

model = tf.keras.models.load_model("classification/ecobc_model.h5")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def classify(request):
    # Get recycling image from the user, and input to the recycling classification model
    if request.method == 'POST':
        image=request.FILES['image']
        data = predict.predict(image.read(), os.path.splitext(image.name)[1], model)

        # If user recycling is determined to be more than 40%, then the user will gain +1 point
        if data['certainty'] > 0.4:
            try:

                models.Points.objects.filter(user=Token.objects.get(key=request.auth.key).user).update(score=models.Points.objects.get(user=request.user).score + 1)
            except models.Points.DoesNotExist:
                models.Points.objects.create(user=Token.objects.get(key=request.auth.key).user, score=1)

        return Response({"response": "Classify Successful", "type" : data['item']}, status=status.HTTP_200_OK)
    return Response({"response": "Error: Invalid request"}, status=status.HTTP_400_BAD_REQUEST)