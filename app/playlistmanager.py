import sys
sys.path.insert(0, '/Users/Christina/projects/spotify') 
from test_spotipy import get_all_playlists
from test_spotipy import get_all_tracks
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!'

# @app.route('/playlists')
# def playlists():
#     playlists = get_all_playlists(None)
#     return render_template("main.html", playlist=playlist)

@app.route('/test') #trying to test using instructions from this site, but it isn't working: https://www.techiediaries.com/flask-tutorial-templates/
def test():
    return render_template("index.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5'])

# @app.route('/tracks')
# def tracks():
#   print('all tracks')
#   return get_all_tracks(None)
