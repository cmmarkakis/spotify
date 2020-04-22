from test_spotipy import get_all_playlists, get_playlist_titles, get_all_tracks
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/playlistnames')
def playlist_names():
    playlist_names = get_playlist_titles(None)
    return render_template('playlist_names.html', message='Hello Flask!', playlist_names = playlist_names)

@app.route('/playlistdata')
def playlist_data():
    playlist_data = get_all_playlists(None)
    return render_template('all_playlists.html', message='Hello Flask!', playlist_data = playlist_data)

@app.route('/test') #trying to test using instructions from this site, but it isn't working: https://www.techiediaries.com/flask-tutorial-templates/
def test():
    return render_template('test.html', message='Hello Flask!', contacts = ['c1', 'c2', 'c3', 'c4', 'c5'])

#@app.route('/tracks')
