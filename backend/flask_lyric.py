from flask import Flask, jsonify, request
from LyricAPI import get_game_lyrics, get_lyrics
from spotipy_searches import *


app = Flask(__name__)

@app.route("/api/lyrics", methods=["POST"])
def send_data():

    receive = request.json # will receive artist(s)
    
    print(receive)

    big_data = []

    if len(list(receive) == 1):
        artist = list(receive)[0]
        songs = search_by_artist(artist)

        for song in songs:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))

    else:
        lst_of_tuple = search_by_x_artists(tuple(receive))

        for song, artist in lst_of_tuple:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))
    

    return jsonify(big_data)

