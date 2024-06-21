# from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os

def moved(request):
    return JsonResponse({ 'endpoint': 'Working endpoint is /api/v1'})

def download_video(request):
    url = request.GET.get('urls')
    download_path = request.GET.get('download_path', '')

    if not url:
        return JsonResponse({'Error': 'No URL provided'})

    if not download_path:
        download_path = os.getcwd()

    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(download_path)
        return JsonResponse({'video': 'Video downloaded successfully', 'path': download_path})
    except Exception as e:
        return JsonResponse({'Error': str(e)})
