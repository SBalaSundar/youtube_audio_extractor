from pytube import YouTube

# where to save
destination = "/home/balasundar/Downloads/"
# link of the video to be downloaded
video_link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
    video = YouTube(video_link)
    # filtering the audio. File extension can be mp4/webm
    # You can see all the available streams by print(video.streams)
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download()
    print('Task Completed!')
    
except:
    print("Connection Error")  # to handle exception
