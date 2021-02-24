from youtube_api import YouTubeDataAPI
import json

def getAllUrlVideoOfChannel(channel_id, api_key):
    yt = YouTubeDataAPI(api_key)
    channels = yt.get_playlists(channel_id)
    videoUrls = []
    for i in range(len(channels)):
        videoOfPlaylist = yt.get_videos_from_playlist_id(channels[i]['playlist_id'])
        for j in range(len(videoOfPlaylist)):
            videoUrls.append('https://www.youtube.com/watch?v=' + videoOfPlaylist[j]['video_id'])

    return videoUrls

def dataToJsonFile(data):
    with open('data_sitcom.json', 'w', encoding='utf8') as txt_file:
        json.dump(data, txt_file, ensure_ascii=False)

# channel_id='UCmuhxjDBXmaR4a3orGUVeRA'
channel_id='UC3zfPvWBcI1Da9TQI0XJCQA'
api_key='AIzaSyAp-9SwAWTLRo08WSzFcBaKQOPmt3Bczdw'


dataToJsonFile(getAllUrlVideoOfChannel(channel_id=channel_id, api_key=api_key))