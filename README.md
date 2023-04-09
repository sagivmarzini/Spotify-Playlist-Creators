# Spotify Python Scripts
This repository contains two Python scripts for interacting with the Spotify API using the spotipy library.

## Installation
1. Clone the repository to your local machine.
2. Install the spotipy library by running pip install spotipy in your command line.
3. Replace the client_id and client_secret values in each script with your own Spotify API credentials.
4. Run the scripts using python script_name.py.


## Script Descriptions
### [Script 1](Text2Playlist.py): Create a Playlist from a List of Songs
This script prompts the user to enter a list of song names and a playlist name. It then creates a new public playlist on the user's Spotify account and searches for each song in the list, adding the first result to the playlist.

### Script 2: Combine Two Playlists into One
This script prompts the user to enter the URLs of two Spotify playlists. It then retrieves all tracks from both playlists, removes duplicates, and creates a new public playlist with the combined tracks.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
