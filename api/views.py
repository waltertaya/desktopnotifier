# from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os

def download_video(request):
    url = request.GET.get('urls')
    download_path = request.GET.get('download_path', '')  # Default to current directory if not provided

    if not url:
        return JsonResponse({'Error': 'No URL provided'})

    if not download_path:
        download_path = os.getcwd()  # Use current directory if no path is provided

    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(download_path)
        print("Video downloaded successfully!")
        return JsonResponse({'video': 'Video downloaded successfully', 'path': download_path})
    except Exception as e:
        print("An error occurred while downloading the video:", str(e))
        return JsonResponse({'Error': str(e)})
