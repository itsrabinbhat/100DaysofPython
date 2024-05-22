from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


sp = Spotify(auth_manager=SpotifyOAuth(client_id="0b34a21a6fa746079e02c3daf617de8c",
                                       client_secret="22bb1056d97f45eb9b74bc0b55402599",
                                       scope="playlist-modify-private",
                                       redirect_uri="http://example.com",
                                       show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()['id']

# Scrapping songs from bill board
user_input = input("Which year you want to travel to?(YYYY-MM-DD): ")
res = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_input}")
songs_data = BeautifulSoup(res.text, 'html.parser')
playlist = songs_data.select('div ul li ul li h3')
playlist = [song.getText().strip() for song in playlist]


