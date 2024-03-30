from helper_functions import downloader

# file_name  = downloader("https://www.youtube.com/watch?v=j-2y-ZYezIo")
file_name  = 'WWE 2K24 - Official Launch Trailer.mp4'
print(file_name)


from moviepy.editor import VideoFileClip

VideoFileClip(file_name).write_videofile("output_video.mp4", codec='.mp4v', audio=False)

# clip_resized= clip.resize(height=1920)
# clip_resized.write_videofile("output_video.mp4")

# clip_resized.ipython_display()