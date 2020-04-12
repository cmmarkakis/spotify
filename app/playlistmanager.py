from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/playlists')
def playlists():
    print()
    return 'List of all users playlists'


@app.route('/tracks')
def tracks():
  print('all tracks')
  return 'List of all tracks in a given playlist'
