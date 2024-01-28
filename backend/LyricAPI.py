import json
import requests
from secret import *
import random

def get_lyrics(artist: str, song_name: str) -> list:
    '''
    Parameters:
    artist: str
    song_name: str

    Returns:
    List object of lyrics

    Sends a request to lyrics.ovh API to get song lyrics
    Processes lyrics and whitespaces
    '''

    lyrics = []

    r = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song_name}")

    if r.status_code == 200:

        lyrics = r.json()["lyrics"].split('\n')

        ct = 0

        for i in lyrics:
            if i == "":
                ct += 1

        for i in range(ct):
            lyrics.remove("")
    
    return lyrics


def get_game_lyrics(lyrics: list) -> str:

    if lyrics != []:

        lyric_str_len = 0

        while lyric_str_len <= 2:
            i = random.randint(0, len(lyrics))

            temp_lyric = lyrics[i]

            for e in temp_lyric:
                if e in ("<>?/\][]{}+-=;.,"):
                    temp_lyric.replace(e, "")
            
            lyric_str_len = len(temp_lyric.split())


        if len(lyric_str_len) == 3 or len(lyric_str_len) == 4:

            index = which_chunk(1, lyric_str_len)

        elif len(lyric_str_len) == 5:

            index = _randomness(5, temp_lyric)

        elif len(lyric_str_len) >= 6:

            index = _randomness(6, temp_lyric)

    return index


def _randomness(size_str, string):

    chance = random.randint(0, 2)

    index = []

    if (chance == 0):
        return [random.randint(0, size_str)]

    elif (chance == 1):
        # ALWAYS REMOVES 2, BUT IF LEN 6 CAN REMOVE 3
        if size_str == 5:
            index = which_chunk(2, len(string))
           
        else:
            chance = random.randint(0, 2) # chance to remove 3
            if (chance == 0):
                index = which_chunk(2, len(string))
            else:
                index = which_chunk(3, len(string))

    return index


def which_chunk(remove_size: int, size_str):

    index = []

    i = random.randint(0, 3)

    if (i == 0):
        # remove from the front
        index = [i for i in range(remove_size)]

    elif (i == 1):
        # remove from the middle
        index = [(size_str // 2) + i for i in range(remove_size)]

    else:
        # remove from the back
        index = [(i + 1) * -1 for i in range(remove_size)]

    return index

# def non_duplicates(indicies: list, string: str, need_size: int):

#     while need_size < len(indicies):

#         i = random.randint(0, len(string))

#         if i not in indicies:
#             indicies.append(i)

#     return indicies


lst = get_lyrics("keshi", "understand")
