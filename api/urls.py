from django.urls import path, include
from . import views

urlpatterns = [
    path('api/v1/', views.download_video, name='download_video')
]
