import requests
import spotipy
import spotipy.util as util
import json

def get_spotify_token(username, client_id, client_secret, redirect_uri):
    # get token

    token = util.prompt_for_user_token(username, scope='playlist-modify-public',
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    return token


def create_playlist(playlist_name, token, username):

    sp = spotipy.Spotify(auth=token)

    # Check if playlist name exists:
    get_playlists = sp.user_playlists(username)
    playlists = get_playlists['items']
    if playlist_name in [n['name'] for n in playlists]:
        raise Exception(f"A Playlist Named: {playlist_name} already exists")


    # Create playlist
    endpoint_url = f"https://api.spotify.com/v1/users/{username}/playlists"
    request_body = json.dumps({
        "name": playlist_name,
        "public": True
    })
    response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                               "Authorization": "Bearer " + token})

    playlist_id = response.json()['id']
    return playlist_id


def add_tracks(songs, artist, token, username, playlist_id):

    sp = spotipy.Spotify(auth=token)
    tracks_ids = []

    for song in songs:
            # Check if each track exists
            track_ids = sp.search(q='artist:' + artist + ' track:' + song, type='track', limit=1)
            tracks = track_ids['tracks']
            items = tracks['items']

            try:
                item = items[0]
                tracks_ids.append(item['id'])
            except:
                print(f'The song: {artist} - {song}  was not found on spotify')
                continue
    # Add tracks to playlist
    sp.user_playlist_add_tracks(username, playlist_id, tracks=tracks_ids)
    print('Playlist Created')
    return