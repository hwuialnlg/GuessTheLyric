from secret import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_PASS)
SP = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_by_artist(artist: str, limit: int) -> [str]:
    '''
    Retrieve a list of song names made by the inputted artist. Songs will be retrieved from Spotify.

    Args:
        artist: The name of the artist to search songs for
        limit: the maximum amount of songs to search for from the artist
    
    Returns:
        A list of songs made by the inputted artist.
    '''
    artist = artist.lower() # name of artists case-sensitive
    song_names = [] # list to store names of songs

    results = SP.search(artist, limit, type='track') # Spotipy querying results from an artist
    for track in results['tracks']['items']:
        # Only add the song if the it is made by the inputted artist and not a related artist
        if track['artists'][0]['name'].lower() == artist: 
            song_names.append(track['name'])
    return song_names

def search_by_x_artists(artists: (str), limit: int) -> [str]:
    '''
    Retrieve a list of song names made by any of the inputted artists. Songs will be retrieved from Spotify.

    Args:
        artists: A tuple of artist names to search songs for
        limit: the maximum amount of songs to search for from each artist
    
    Returns:
        A list of songs made by any of the inputted artists.
    '''
    song_names = [] # list to store names of songs
    for artist in artists:
        songs = search_by_artist(artist, limit) # returns a list of song names from the the current artist
        song_names.extend(songs)
    return song_names

def search_by_playlist(playlist_url: str) -> [str]:
    '''
    Retrieve a list of song names from a user inputted Spotify playlist.

    Args:
        playlist_url: string representing a URL to a Spotify playlist to get songs from
    
    Returns:
        A list of songs from a user inputted Spotify playlist.
    '''
    # Get rid of any query fragment/parameters in the link
    # Get the id of the playlist which is after the last slash in the link
    playlist_id = playlist_url.split('?')[0].split('/')[-1] if '?' in playlist_url \
        else playlist_url.split('/')[-1]

    song_names = [] # list to store names of songs
    results = SP.playlist(playlist_id) # Spotipy querying results from a playlist

    tracks = results['tracks'] 
    while tracks: # Checks if there are still tracks to iterate over
        for track in tracks['items']:
            song_names.append(track['track']['name'])
        tracks = SP.next(tracks) # If the playlist has more than 100 songs, go the next page of songs to get
    return song_names
    
if __name__ == "__main__":
    # print(search_by_artist('keshi', 30))
    # print(search_by_x_artists(('keshi', 'dpr ian'), 30))
    print(search_by_playlist('https://open.spotify.com/playlist/3c8sZa0lI8eWU9aJpr3w2M'))
    # search_by_playlist('https://open.spotify.com/playlist/5iUayjyzc0JuftsOHIaWb1?si=d62809d69cf2406c')