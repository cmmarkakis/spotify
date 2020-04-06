import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

##Seting environmental variables in terminal for Mac
export SPOTIPY_CLIENT_ID=#####
export SPOTIPY_CLIENT_SECRET=#####
SPOTIPY_REDIRECT_URI=#######

scope = playlist-read-private


#This function should return all of your playlists

def get_all_playlists(username):
    playlists = sp.current_user_playlists(username) #got from spotipy documentation: https://readthedocs.org/projects/spotipy/downloads/pdf/latest/
    playlist_list=[]
    for playlist in playlists["items"]:
        playlist_list.append(playlist['name'])) #made in case we want to use it as a list later
        print()
        print(playlist['name'])

#This function shoudl return all the tracks of a given playlist
def get_all_tracks(playlist):
    return


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
