# import json
from secret import *
# import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_PASS)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_query = 'keshi'
results = sp.search(artist_query, 30, type='track')
print(type(results))
for i in results['tracks']['items']:
    if i['artists'][0]['name'] == artist_query:
        print(i['name'])
    # if i['artists']['name'] == artist_query:
    # print(i.keys())
    # print(i['artists'][0]['name'])
    # print(i['name'])

