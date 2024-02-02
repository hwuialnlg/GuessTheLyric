import json
import requests
from secret import *
import random

def get_lyrics(artist: str, song_name: str) -> list:
    '''
    Parameters:
    artist type str, which is the artist's name
    song_name type str, which is the song's name

    Returns:
    List object of lyrics from the song

    Explanation:
    Sends a request to lyrics.ovh API to get song lyrics
    Processes lyrics and whitespaces
    '''
    lyrics = []
    
    print(artist)

    r = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song_name}")

    if r.status_code == 200:

        lyrics = r.json()["lyrics"].split('\n')

        ct = 0

        for i in lyrics:
            if i == "":
                ct += 1

        for i in range(ct):
            lyrics.remove("")

        for i in range(len(lyrics)):
            lyrics[i] = lyrics[i].rstrip()
    
        return lyrics
    
    return -1


def get_game_lyrics(artist: str, lyrics: list[str], song_name: str) -> tuple:
    '''
    Parameters:
    artist type str, the artist of the song
    lyrics type lists, contains all lyrics of the song
    song_name type str, song name 

    Returns:
    Tuple containing song name, the chunk of lyric, and list of indicies to remove from chunk

    Explanation:
    This function looks for a lyric chunk that is greater than size two to be used 
    and process to remove extra unnecessary characters. This function puts together
    the helper function to return necessary data for the game.
    
    '''

    lyric_str_len = 0

    temp_lyric = None

    if lyrics != []:
        lyrics.pop(0)

    # print(len(lyrics))
    # print(lyrics)

    while lyric_str_len <= 2:
        i = random.randint(0, len(lyrics)-1)
        # print(i)

        temp_lyric = lyrics[i]

        for e in temp_lyric:
            if e in ("<>?/\][]{}+-=;.,"):
                temp_lyric.replace(e, "")
        
        lyric_str_len = len(temp_lyric.split())
        # print(lyric_str_len)

    if lyric_str_len == 3 or lyric_str_len == 4:
        # print(3, 4)
        index = _which_chunk(1, temp_lyric)

    elif lyric_str_len == 5:
        # print(5)
        index = _randomness(5, temp_lyric)
        # print(index)

    elif lyric_str_len >= 6:
        # print(6)
        index = _randomness(6, temp_lyric)

    # print(lyrics) 
            
    # print(temp_lyric, index)

    return (artist, song_name, temp_lyric, index)


def _randomness(size_str: int, string: str) -> list[int]:
    '''
    Parameters:
    size_str type int, size of the lyric chunk
    string type str, the lyric chunk itself

    Returns:
    List of integers that contain where to remove from

    Explanation:
    This helper function decides how many times to remove
    from a lyric chunk given the size. The randomness is at
    certain sizes the function will potentially remove more words.
    '''
    chance = random.randint(0, 1)

    index = []

    if (chance == 0):
        # print("REMOVE 1")
        return [random.randint(0, size_str-1)]

    elif (chance == 1):
        # ALWAYS REMOVES 2, BUT IF LEN 6 CAN REMOVE 3
        # print("TEST 2")
        if size_str == 5:
            index = _which_chunk(2, string)
           
        else:
            chance = random.randint(0, 1) # chance to remove 3
            # print("TEST 1")
            if (chance == 0):
                index = _which_chunk(2, string)
            else:
                # print("TEST")
                index = _which_chunk(3, string)

    return index


def _which_chunk(remove_size: int, string: str) -> list[int]:
    '''
    Parameters: 
    remove_size type int, how much words to remove
    size_str type int, what the length of the lyric chunk is

    Returns:
    a list of indicies to remove from the lyric chunk

    Explanation:
    This helper function randomly determines whether to remove from the
    beginning, middle, or end of the lyric chunk. 
    '''
    index = []

    i = random.randint(0, 2)

    if (i == 0):
        # print("FRONT")
        # remove from the front
        index = [i for i in range(remove_size)]

    elif (i == 1):
        # remove from the middle
        # print("MIDDLE")
        index = [((len(string.split())-1) // 2) + i for i in range(remove_size)]

    else:
        # remove from the back
        # print("END")
        # index = [(i + 1) * -1 for i in range(remove_size)]

        index = [len(string.split()) - 1 - i for i in range(remove_size)]

    return index

# def non_duplicates(indicies: list, string: str, need_size: int):

#     while need_size < len(indicies):

#         i = random.randint(0, len(string))

#         if i not in indicies:
#             indicies.append(i)

#     return indicies


# lst = get_lyrics("keshi", "understand")

# print(get_game_lyrics("keshi", lst, "understand"))
