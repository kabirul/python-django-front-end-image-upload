from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.upload_image, name='upload-image'),
]