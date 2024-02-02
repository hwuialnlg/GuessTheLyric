from LyricAPI import get_game_lyrics, get_lyrics
from spotipy_searches import *


if __name__ == "__main__":

    artist = input("Input your artist: ")

    songs_tpl = search_by_artist(artist)

    print(get_lyrics(songs_tpl[0][1], songs_tpl[0][0]))