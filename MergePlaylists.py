import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create a Spotify object with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="04d6212df181483da554c458885543da",
                                               client_secret="2e396bb44629499abe2f50ca3695ede1",
                                               redirect_uri="http://localhost:8080/callback/",
                                               scope="playlist-modify-public"))

# Get user input for two playlist URLs
playlist1_url = input("Enter the first playlist URL: ")
playlist2_url = input("Enter the second playlist URL: ")

# Get playlist IDs from playlist URLs
playlist1_id = playlist1_url.split("/")[-1]
playlist2_id = playlist2_url.split("/")[-1]

# Get all tracks from playlist1
playlist1_tracks = []
offset = 0
while True:
    results = sp.playlist_items(playlist1_id, offset=offset)
    playlist1_tracks.extend(results["items"])
    offset += len(results["items"])
    if len(results["items"]) == 0:
        break

# Get all tracks from playlist2
playlist2_tracks = []
offset = 0
while True:
    results = sp.playlist_items(playlist2_id, offset=offset)
    playlist2_tracks.extend(results["items"])
    offset += len(results["items"])
    if len(results["items"]) == 0:
        break

# Combine the tracks from the two playlists and remove duplicates
combined_tracks = list(set([track["track"]["id"] for track in playlist1_tracks + playlist2_tracks]))

# Create a new playlist with the combined tracks
new_playlist = sp.user_playlist_create(user=sp.current_user()["id"], name="Combined Playlist", public=True)

# Add tracks to the new playlist in batches of 100
for i in range(0, len(combined_tracks), 100):
    track_uris = combined_tracks[i:i + 100]
    sp.playlist_add_items(new_playlist["id"], track_uris)

print(f"Combined playlist '{new_playlist['name']}' created with {len(combined_tracks)} tracks.")