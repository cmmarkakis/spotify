from spotipy_api import get_all_playlists, get_playlist_titles, get_all_tracks
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/playlists')
def playlist_names():
    playlist_names = get_all_playlists(None)
    return jsonify(playlist_names)


@app.route('/playlist/detail/<playlist_id>')
def playlist_data(playlist_id):
    playlist_data = get_all_tracks(playlist_id)
    return jsonify(playlist_data)