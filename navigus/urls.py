from django.contrib import admin
from django.urls import path , include

from contact import urls
from feedback import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path ("" , include('contact.urls')),
    path ("" , include('feedback.urls'))
]
