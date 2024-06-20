from django.urls import path
from .views import download_video, moved

urlpatterns = [
    path('api/v1/', download_video, name='download_video'),
    path('api/v1/moved', moved, name='moved')
]
