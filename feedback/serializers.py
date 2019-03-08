from rest_framework import serializers
from .models import *

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class FeedbackOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("location" , )