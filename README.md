# Spotify Duplicate Tracks
Find duplicate tracks in Spotify playlists.

Spotify Duplicate Track is used to find duplicate tracks in a Spotify playlist. The Spotify web client doesn't prompt users to `Skip duplicate` or `Add duplicate` when adding duplicate track to a playlist like the desktop and mobile clients. This can lead users to unknowingly add multiple copies of the same track to a playlist. This script can help users find these tracks.

  - Only user library read permission is granted, so no changes will be made to your account.
  - Shows only playlists you own.
  - Magic...idk🤓

### Libraries

Spotify Duplicate Track uses the following of open source project to work properly:

* [Spotipy](http://spotipy.readthedocs.org/) - Spotipy is a lightweight Python library for the Spotify Web API.


### Installation

Spotify Duplicate Tracks requires [Python](https://www.python.org/) 3+ to run.

Install the dependencies.

```
pip install spotipy
```

or upgrade

```
pip install spotipy --upgrade
```

### Run script
With the Spotify account associated with the playlist you wish to check for duplicate tracks, create a new project on the [Spotify developer](https://developer.spotify.com/dashboard/) website.
* Make a note of the project's Client ID and Client Secret values.
* Set the redirect url to: `"http://localhost:8080"`.

1) Copy the Client ID, Client Secret and username to `client_id`, `client_secret` and `username` in their respective variables in the script. The redirect url is already hardcoded in the script.

2) Launch script
```
python duplicate_tracks.py
```
3) If the redirect url is changed, you will be asked to copy a link from your browser to command line.
4) Select the playlist you would like to be checked and wait a few seconds.
5) View the names of the tracks and manually remove them if desired by searching the playlist.


License
----

MIT


