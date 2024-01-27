import json
import requests
from secret import *

def get_lyrics(artist: str, song_name: str) -> list:
    '''
    Parameters:
    artist: str
    song_name: str

    Returns:
    List object of lyrics

    Sends a request to lyrics.ovh API to get song lyrics
    '''

    r = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song_name}")

    lyrics = r.json()["lyrics"].split('\n')

    ct = 0

    for i in lyrics:
        if i == "":
            ct += 1

    for i in range(ct):
        lyrics.remove("")
    
    return lyrics