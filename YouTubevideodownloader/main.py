from pytube import YouTube

def download_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred while downloading the video:", str(e))

# Example usage
video_url = "https://www.youtube.com/shorts/toZ35X_I_XI"  # Replace with your video URL
download_video(video_url)
