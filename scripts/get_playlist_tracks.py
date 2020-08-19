import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 


client_id = 'client id'
client_secret = 'client secret'


creds = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=creds)


#function to grab playlist from user
def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids


#grab data from track
def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    #main track items
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    #track features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    instrumentalness = features[0]['instrumentalness']
    loudness = features[0]['loudness']
    tempo = features[0]['tempo']
    speechiness = features[0]['speechiness']
    valence = features[0]['valence']
    time_signature = features[0]['time_signature']


    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, instrumentalness, loudness, tempo, speechiness, valence, time_signature]
    return track


#grab tracks
tracks = []

for i in range(len(ids)):
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)
    

df = pd.DataFrame(tracks,
                 columns = ['name',
                            'album',
                            'artist',
                            'release_date',
                            'length',
                            'popularity',
                            'danceability',
                            'acousticness',
                            'danceability',
                            'instrumentalness',
                            'loudness',
                            'tempo',
                            'speechiness',
                            'valence',
                            'time_signature'])