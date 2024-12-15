import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def load_playlists(file_path):
    """Load playlists data from a JSON file"""
    with open(file_path) as file:
        return json.load(file)
    
def load_credentials(credentials_path):
    """Getting just de API address"""
    with open(credentials_path) as file:
        return json.load(file)
    

    
playlists_data = load_playlists('exported_files/playlists.json')

playlist_items = playlists_data.get('items',[])

playlist_info = [(playlist['id'],playlist['name'] ) for  playlist in playlist_items]

credentials = load_credentials('credentials.json')

client_id = credentials['client_id']
client_secret = credentials['client_secret']
redirect_uri = credentials['redirect_uri']
scope = credentials['scope']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

my_playlists = {}

for playlist, playlist_name in playlist_info:
    songs = sp.playlist_items(playlist_id=playlist)
    my_playlists[playlist] = {"name": playlist_name,
                               "content": songs}

    
    

with open("exported_files/playlist_content.json", "w") as file:
    json.dump(my_playlists, file)