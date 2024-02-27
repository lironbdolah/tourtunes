from scrape_setlist_fm import *
from spotipy_playlist import *



if __name__ == '__main__':

    url = input('Enter the Setlist URL: ')
    user_name = input('Enter your Spotify username: ')
    client_id = input('Enter your Spotify Client ID: ')
    client_secret = input('Enter your Spotify Client secret: ')
    redirect_url = input('Enter your Spotify Redirect URL: ')

    artist,songs,playlist_name = retrive_songs(url)
    token = get_spotify_token(user_name,client_id,client_secret,redirect_url)
    playlist_id = create_playlist(playlist_name,token,user_name)
    add_tracks(songs,artist,token,user_name, playlist_id)


