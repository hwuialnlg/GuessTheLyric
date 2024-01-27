# import json
from secret import *
# import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_PASS)
SP = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_by_artist(artist: str, limit: int) -> [str]:
    songs = []
    results = SP.search(artist, limit, type='track')
    for i in results['tracks']['items']:
        if i['artists'][0]['name'] == artist:
            songs.append(i['name'])
    return songs

if __name__ == "__main__":
    print(search_by_artist('keshi', 30))
