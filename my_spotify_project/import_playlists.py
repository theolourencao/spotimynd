import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json



client_id = '977fead8e35544e3bf7580ec5516d57c'
client_secret = 'e03b92e4a2a84fef8be0e2394f5ac084'
redirect_uri = 'http://localhost:8888/callback/'
scope = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

playlists = sp.current_user_playlists()

with open("exported_files/playlists.json", "w") as file:
    json.dump(playlists, file)

for playlist in playlists['items']:
    print(f"Playlist: {playlist['name']}")