
from django.contrib import admin
from django.urls import path , include
from rest_framework.documentation import include_docs_urls
from .views import *

 
urlpatterns = [
        path("feedback/", FeedbackView.as_view())
]
