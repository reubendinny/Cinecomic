from pytube import YouTube


def download_video(link):
    SAVE_PATH = "video/" 

    try: 
        yt = YouTube(link) 
    except: 
        print("Connection Error") 

    # Get all streams and filter for mp4 files
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    try: 
        # downloading the video 
        d_video.download(output_path=SAVE_PATH, filename="uploaded.mp4")
        print('Video downloaded successfully!')
    except: 
        print("Some Error!")

download_video("https://www.youtube.com/watch?v=wdmSrEUhjwQ")