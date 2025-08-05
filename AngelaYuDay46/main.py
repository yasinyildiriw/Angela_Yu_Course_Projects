import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URL = "http://127.0.0.1:8888/callback"
USER = ""

url = "https://www.billboard.com/charts/hot-100/"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(url=f"{url}{year}/", headers=header)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
songs = soup.select("li h3.c-title")
songs_list = [sing.get_text(strip=True) for sing in songs]
singers = soup.select("li ul li span.c-label")
singer_list = [sarkici.get_text(strip=True) for sarkici in singers]
# print(songs_list)
# print(singer_list)
filtered_singer_list = []
for i in singer_list:
    try:
        if int(i) < 1000:
            continue
    except ValueError:
        pass
    filtered_singer_list.append(i)
# print(filtered_singer_list)
sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = REDIRECT_URL,
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        show_dialog = True,
        cache_path = "token.txt",
    )
)
user_id = sp.current_user()["id"]
track_uris = []
for song,singer in zip(songs_list, filtered_singer_list) :
    query = f"track:{song} artist:{singer}"
    try:
        result = sp.search(q=query, type="track", limit=1)
        track = result["tracks"]["items"][0]
        uri = track["uri"]
        track_uris.append(uri)
        print(f"✅ Found: {song} - {singer}")
    except (IndexError, KeyError):
        print(f"❌ Not found on Spotify: {song} - {singer}")
print(len(track_uris))
print(track_uris)

playlist_name = f"{year} Billboard 100"
playlist = sp.user_playlist_create(
    user = USER,
    name = playlist_name,
    public = False
)
playlist_id = playlist["id"]
print(f"🎉 Created playlist: {playlist_name} (ID: {playlist_id})")

sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
print(f"✅ Added {len(track_uris)} songs to playlist!")

