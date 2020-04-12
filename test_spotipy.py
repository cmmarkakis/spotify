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
    all_playlists = {}

    playlists = sp.user_playlists(username)

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            all_playlists.update({playlist['uri']:playlist['name']})
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return all_playlists


def get_all_tracks(playlist_id):
    '''
    assumes we have the playlist_id
    Parameters
    ----------
    playlist_id : TYPE
        DESCRIPTION.

    Returns
    -------
    Prints all the tracks of a given playlist

    '''
    playlist_tracks = sp.playlist_tracks(playlist_id)
    for track in playlist_track['items']:
        print()
        print(track['album']['name'])


def get_all_tracks(playlist):
    results = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/
    if playlist in results['items']:
        for item in results['item']: #looking through every item in the data we get from api
            playlist_id = results['item']['id']
            playlist_tracks = sp.playlist_tracks(playlist_id)
            return results['item']['name'] + playlist_tracks
    else:
        print('Playlist not found')

if __name__ == "__main__":
    print('write functions')
