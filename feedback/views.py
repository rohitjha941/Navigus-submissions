from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.forms.models import model_to_dict
from .models import *


class FeedbackView(APIView):
    serializer_class = FeedbackSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

    def options(self, request):
        feedback = Feedback.objects.all()
        location = []
        for f in feedback:
            location.append(f.location)
        data = {
            "location" : location
        }
        return Response(data = data, status=status.HTTP_200_OK)
        
