import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

##Seting environmental variables in terminal for Mac
# export SPOTIPY_CLIENT_ID=#####
# export SPOTIPY_CLIENT_SECRET=#####
# SPOTIPY_REDIRECT_URI=#######

def get_all_playlists(username):
    '''
    Parameters
    ----------
    username : TYPE
        DESCRIPTION.

    Returns
    -------
    A list of dictionaries, where one dictionary represents the attributes a single playlist
    '''
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    all_playlists = []

    playlists = sp.user_playlists('cmarkz133')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            all_playlists.append({'uri': playlist['uri'], 'name':playlist['name']})
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return all_playlists

def get_playlist_titles(playlists):
    playlist_titles = []
    playlists = get_all_playlists(None)
    for value in playlists.values():
        playlist_titles.append(value)
    #playlist has playlistid as the key and playlist name as the value
    return playlist_titles


def get_all_tracks(playlist_id):
    '''
    assumes we have the playlist_id
    Parameters
    ----------
    playlist_id : TYPE
        DESCRIPTION.

    Returns
    -------
    A list of dictionaries representing each track in a playlist

    '''
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist_tracks = sp.playlist_tracks(playlist_id)

    all_results = []

    for track in playlist_tracks['items']:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        all_results.append({'song_name':song_name, 'artist_name':artist_name})

    return all_results

if __name__ == "__main__":
    print(get_all_playlists(None))
