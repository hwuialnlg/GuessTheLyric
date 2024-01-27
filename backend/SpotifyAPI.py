import json
from secret import *
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import util

SCOPE = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

# token = util.prompt_for_user_token(USERNAME)

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)


