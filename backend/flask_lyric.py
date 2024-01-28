from flask import Flask, jsonify, request
from LyricAPI import get_game_lyrics, get_lyrics
from spotipy_searches import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/lyrics", methods=["POST"])
def send_lyric_data():
    '''
    Flask connection sending backend lyric, artist, and song data to frontend
    '''
    receive = request.json['message'] # will receive artist(s)
    
    print(receive)

    big_data = []

    if len(receive[0]) == 1:
        artist = receive[0][0]
        songs = search_by_artist(artist)

        # img = get_artist_pic(artist)

        for song, artist in songs:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))

    else:
        lst_of_tuple = search_by_x_artists(tuple(receive[0]))

        for song, artist in lst_of_tuple:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))
    

    return jsonify({'response': big_data})


@app.route("/image", methods=["POST"])
def send_image():
    '''
    Flask connection sending backend of image to frontend
    '''
    receive = request.json['message'] # will receive artist(s)
    
    print(receive)

    dct = {}

    if len(receive[0]) == 1:
        artist = receive[0][0]

        dct = get_artist_pic(artist)

    else:

       dct = get_artist_pics({artist for song, artist in receive[0]})

    return jsonify({'response': dct})


if __name__ == '__main__':
    app.run(debug=True)