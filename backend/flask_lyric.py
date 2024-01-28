from flask import Flask, jsonify, request
from LyricAPI import get_game_lyrics, get_lyrics
from spotipy_searches import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/lyrics", methods=["POST"])
def send_data():

    receive = request.json['message'] # will receive artist(s)
    
    print(receive)

    big_data = []
# [['Nav', 'The Weekend'], '6']
    if len(receive[0]) == 1:
        artist = receive[0][0]
        songs = search_by_artist(artist)

        for song, artist in songs:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))

    else:
        lst_of_tuple = search_by_x_artists(tuple(receive[0]))

        for song, artist in lst_of_tuple:
            big_data.append(get_game_lyrics(artist, get_lyrics(artist, song), song))
    

    return jsonify({'response': big_data})

if __name__ == '__main__':
    app.run(debug=True)