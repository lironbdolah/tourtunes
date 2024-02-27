from bs4 import BeautifulSoup
import requests

def retrive_songs(url):

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html")
    artist = soup.find('h1').find('span').text
    venue =soup.find('h1').find_all('span')[4].text
    playlist_name = f"{artist} - {venue}"
    songs = []

    for song_tag in soup.find_all("a", {"class": "songLabel"}):
        songs.append(song_tag.contents[0])

    return artist,songs,playlist_name