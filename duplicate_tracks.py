import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set values here or set as os environment variables
client_id = ""
client_secret = ""

scope = "user-library-read"
redirect_uri = "http://localhost:8080"
username = ""
cache_path = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, cache_path=cache_path, username=username))

# Get current user profile 
current_user = sp.me()
print("Name: {0} - URI: {1} - Spotify URL: {2}".format(current_user['display_name'], current_user['uri'], current_user['external_urls']['spotify']))

# Get user owned playlists
playlists = sp.current_user_playlists()
print("Playlists")
count = 0
my_playlists = []
for playlist in playlists['items']:
    if playlist['owner']['id'] == current_user['id']:
        count += 1
        my_playlists.append(playlist)
        print("{0}) Name: {1} - ID: {2}".format(count, playlist['name'], playlist['id']))

# Prompt user to select playlist
selection = int(input("Select a playlist to check for duplicate songs: "))

# Get the selected playlist
results = sp.playlist(my_playlists[selection-1]['id'], fields="tracks, next")['tracks']
all_tracks = results['items']
while results['next']:
    results = sp.next(results)
    all_tracks.extend(results['items'])

# Print all tracks
# for track in all_tracks:
#   print("{0} - {1}".format(track['track']['artists'][0]['name'], track['track']['name']))

print("Duplicate Tracks")
length = len(all_tracks)
duplicate_tracks = {}
for i in range(length):
    k = i + 1
    for j in range(k, length):
        if all_tracks[i]['track']['id'] == all_tracks[j]['track']['id']:
            duplicate_tracks[all_tracks[j]['track']['id']] = all_tracks[i]  # Add a duplicated track to a dictionary using the track id as the unique key, so only one entry per track is present.

# Show duplicate songs
for track in list(duplicate_tracks.values()):
    print("{0} - {1}".format(track['track']['artists'][0]['name'], track['track']['name']))