from secret import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_PASS)
SP = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_by_artist(artist: str, limit: int) -> [str]:
    '''
    Retrieve a list of song names made by the inputted artist.

    Args:
        artist: The name of the artist to search songs for
        limit: the maximum amount of songs to search for from the artist
    
    Returns:
        A list of songs made by the inputted artist.
    '''
    artist = artist.lower()
    songs = []
    results = SP.search(artist, limit, type='track')
    for i in results['tracks']['items']:
        if i['artists'][0]['name'].lower() == artist:
            songs.append(i['name'])
    return songs

def search_by_x_artists(artists: (str), limit: int) -> [str]:
    '''
    Retrieve a list of song names made by any of the inputted artists.

    Args:
        artists: A tuple of artist names to search songs for
        limit: the maximum amount of songs to search for from each artist
    
    Returns:
        A list of songs made by any of the inputted artists.
    '''
    all_songs = []
    for artist in artists:
        songs = search_by_artist(artist, limit)
        all_songs.extend(songs)
    return all_songs


if __name__ == "__main__":
    print(search_by_artist('keshi', 30))
    print(search_by_x_artists(('keshi', 'dpr ian'), 30))
