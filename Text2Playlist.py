import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get user's input list of song names
song_names = input("Enter a list of song names, separated by commas: ").split(",")

# Set up Spotify authentication using SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="c5845a8ba3ea45938e21128fec3c124f",
                                               client_secret="51bddfa20be145808ccc1a479d6fdff0",
                                               redirect_uri="http://localhost:8080/callback/",
                                               scope="playlist-modify-public"))

# Create a new public playlist
playlist_name = input("Enter the playlist name: ")
playlist = sp.user_playlist_create(user="31ctoymb7fxrq7dkrwhkoa25ucgm", name=playlist_name, public=True)

# Search for each song and add the first result to the playlist
for song_name in song_names:
    results = sp.search(q=song_name, type="track", limit=1)
    if results["tracks"]["items"]:
        track_uri = results["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist["id"], [track_uri])
    else:
        print(f"No results found for {song_name}")

print("PLAYLIST", playlist_name.upper(), "CREATED SUCCESSFULLY")