from django.http import JsonResponse
from pytube import YouTube
import requests
import tempfile
import os
import shutil
import platform

def moved(request):
    return JsonResponse({ 'endpoint': 'Working endpoint is /api/v1'})

def download_video(request):
    url = request.GET.get('url')

    if not url:
        return JsonResponse({ 'Error': 'No URL provided' }, status=400)

    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()

        user_home = os.path.expanduser('~')
        if platform.system() == 'Windows':
            downloads_folder = os.path.join(user_home, 'Downloads')
        elif platform.system() == 'Darwin':  # macOS
            downloads_folder = os.path.join(user_home, 'Downloads')
        else:  # Linux
            downloads_folder = os.path.join(user_home, 'Downloads')

        os.makedirs(downloads_folder, exist_ok=True)

        temp_file_path = os.path.join(downloads_folder, yt.title + '.mp4')
        video_stream.download(output_path=temp_file_path)

        return JsonResponse({ 'Message': 'Video downloaded successfully to Downloads folder.' }, status=200)

    except Exception as e:
        return JsonResponse({ 'Error': str(e) }, status=500)
