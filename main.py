from pytube import *
from moviepy.editor import *
import os

#TODO: 1. Let user choose a directory to which he wants to save a file. (Done)
#      2. Add a dropdown to select a video quality.
#      3. Adapt scripts for particular functions.
#      4. Redesign and colouring.

def get_playlist_video(link, file_path):
    p = Playlist(link)
    print(f"Download {p.title}")
    for video in p.videos:
        stream = video.streams.filter(res="360p").first()
        stream.download(file_path)


def get_audio_only(link, file_path):
    """
    This function allows to download and extract an audio track of a particular YouTube video
    """
    yt = YouTube(link, use_oauth=False, allow_oauth_cache=False)
    print(yt.streams.filter(file_extension='mp4').first()) #idk what it does but let it hang there for a while
    stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
    stream.download(file_path)

    # Bug-tracking part, according to observation script crashes because of the abscence of "."(dot) symbol after the download
    # therefore we are getting "STALKER  2  Heart of Chernobyl Official Trailer.mp4" instead of "S.T.A.L.K.E.R  2  Heart of Chernobyl Official Trailer.mp4"
    # and "BoyWithUke  - Sick of U (Lyrics) ft Oliver Tree.mp4" instead of "BoyWithUke  - Sick of U (Lyrics) ft. Oliver Tree.mp4"

    # with os.scandir('D:\YTLoaderTest') as entries:
    #     for entry in entries:
    #         print(entry.name)
    #         print(f'{stream.title}.mp4')
    #         if entry == (yt.title+'.mp4'):
    #             print("IT'S LITERALLY HERE, WTF IS WRONG")


    #getting rid of the "lost" symbols
    symbols_to_delete = [".", ",", ";", "$", "!", ":"]
    filename = "".join([i for i in stream.title if i not in symbols_to_delete])

    # conversion to mp3
    mp4_file = os.path.join(file_path, f"{filename}.mp4")
    mp3_file = os.path.join(file_path, f"{filename}.mp3")
    #
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    #
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
    #deeting a video fragment for audio only, later will be included to a separate function
    os.remove(os.path.join(file_path, f"{filename}.mp4"))

