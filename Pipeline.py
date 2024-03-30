# %%
from helper_functions import downloader, make_header
import os
import pandas as pd

df = pd.read_csv('data.csv')
frow = df.iloc[0]
game_name = frow.Name
yt_url = frow.yt_url
print(f"{game_name}'s Youtube url is {yt_url}")

file_name  = downloader(yt_url)
print(file_name)

from moviepy.editor import VideoFileClip,  TextClip, CompositeVideoClip, ColorClip, ImageClip, vfx
import moviepy as mp
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

duration = 55
resolution = (1080, 1920)

clip = VideoFileClip(file_name, target_resolution=(720,1280)).subclip(0, duration)
## Create html header
make_header(game_name=game_name, resolution=resolution)

## Resizing and Croppiing
temp_clip = ColorClip(size=resolution, color=(0, 0, 0), duration=duration)
clip_resized = clip.resize(width=1800)
clip_croped = clip_resized.set_pos('center').set_duration(clip_resized.duration)
top_txt_clip = ImageClip('tmp_imp.png', ).set_duration(clip_croped.duration)
video = CompositeVideoClip([temp_clip,top_txt_clip,clip_croped])
video.write_videofile(f"exported_videos/{game_name}.mp4")




