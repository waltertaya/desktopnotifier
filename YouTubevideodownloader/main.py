#!/usr/bin/env python3

from pytube import YouTube
import sys

def download_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred while downloading the video:", str(e))


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        url = sys.argv[1]
    else:
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    download_video(url)
