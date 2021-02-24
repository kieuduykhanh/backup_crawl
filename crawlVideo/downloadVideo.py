import pytube
import json
from moviepy.editor import *
import os


# with open('data.json') as f:
#     data = json.load(f)

with open('data_sitcom.json') as f:
    data = json.load(f)

def downloadVideo(url, num):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    # video.download('./video_file', filename='file{}'.format(num))
    # audio = VideoFileClip('video_file/file{}.mp4'.format(num)).audio
    # audio.write_audiofile('audio_from_video/file{}.mp3'.format(num))
    # os.remove('video_file/file{}.mp4'.format(num))


    video.download('./video_sitcom', filename='file{}'.format(num))
    audio = VideoFileClip('video_sitcom/file{}.mp4'.format(num)).audio
    audio.write_audiofile('audio_sitcom/file{}.mp3'.format(num))
    os.remove('video_sitcom/file{}.mp4'.format(num))

for i in range(0, len(data)):
    try:
        downloadVideo(data[i], i)
        print('done: ', i)
    except Exception as e:
        print('error: ', i)
        print(e)


# url = 'https://www.youtube.com/watch?v=DQR5EqM1doQ'
# youtube = pytube.YouTube(url)
# video = youtube.streams.first()
# video.download(output_path='./video_file', filename='a')
