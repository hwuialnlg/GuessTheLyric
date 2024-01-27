import json
from os import access
from urllib import request, parse
from secret import *
import base64

data = parse.urlencode({
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_PASS,
}).encode()
req =  request.Request(AUTH_URL, data=data) # this will make the method "POST"
resp = request.urlopen(req)

json_data = json.load(resp)

TOKEN_TYPE = json_data["token_type"]
ACCESS_TOKEN = json_data["access_token"]

user_id = input("Input your Spotify User ID\n")

# auth_string = str(base64.b64encode((CLIENT_ID + ":" + CLIENT_PASS).encode("utf-8")), "utf-8")

access_data = parse.urlencode({'Authorization' : "Bearer " + ACCESS_TOKEN})

req_artist = request.Request(f"https://api.spotify.com/v1/me/top/artists", access_data)                       
resp_artists = request.urlopen(req_artist)
json_artists = json.loads(resp_artists)
