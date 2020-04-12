import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

##Seting environmental variables in terminal for Mac
export SPOTIPY_CLIENT_ID=#####
export SPOTIPY_CLIENT_SECRET=#####
SPOTIPY_REDIRECT_URI=#######

scope = playlist-read-private

#OPT 1IF WE WANT TO PRINT INFO AS A RETURN
def get_all_playlists(username):
    '''
    Parameters
    ----------
    username : TYPE
        DESCRIPTION.

    Returns
    -------
    Prints all of a users playlists

    '''
    users_playlists = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/
    for playlist in users_playlists['items']: #looking through every item in the data we get from api     
        print()
        print(playlist['name'])

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
--------
#OPT 2 - IF WE WANT TO STORE DATA AS A RETURN
def get_all_playlists(username):
    '''

    Parameters
    ----------
    username : TYPE
        DESCRIPTION.

    Returns
    -------
    playlist : TYPE
        DESCRIPTION.
    returns all the users playlists

    '''
    results = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/
    for item in results['item']: #looking through every item in the data we get from api
        playlist = items['name']
        return playlist

def get_all_tracks(playlist):
    results = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/
    if playlist in results['items']:
        for item in results['item']: #looking through every item in the data we get from api
            playlist_id = results['item']['id']
            playlist_tracks = sp.playlist_tracks(playlist_id)
            return results['item']['name'] + playlist_tracks
    else:
        print('Playlist not found')

---------    
#OPT 3 -IF WE WANT TO MAKE ONE FUNCTION
username = '' #need to figure out how to get username

def get_user_playlists(username):
    '''
    assumes we know the username
    
    Parameters
    ----------
    username : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.
    Returns a dictionary that has the playlist as the key and all the tracks

    '''
    results = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/ 
    user_playlists = {}
    playlist_id = ''
    
    for playlist in results['items']: #looking through every item in the data we get from api
        playlist_id = results['items']['id']
        userplaylists[results['name']] = get_all_tracks(playlist)
    
    def get_all_tracks(playlist):
        playlist_tracks = sp.playlist_tracks(playlist_id)
        return playlist_tracks results['name']
    
    return user_playlists

----
#bloiler plate sample code
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def fetch_data():
    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

if __name__ == "__main__":
    fetch_data()
