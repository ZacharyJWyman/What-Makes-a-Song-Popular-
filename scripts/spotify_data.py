
import pandas as pd


###
########## 2010 - 2019 songs
###
songs = pd.read_csv(r'/Users/austineaton/Projects/spotify_project/songs.csv')

#Drop unneeded columns
songs.drop(['album', 'Unnamed: 0.1', 'genre', 'popularity_2'], axis = 1, inplace=True)
songs

#Rename 
songs.rename(columns = {'Unnamed: 0':'Number'}, inplace=True)

#Here we find the mean of columns that include NA values
acousticness_mean = songs['acousticness'].mean()
instrumentalness_mean = songs['instrumentalness'].mean()
time_signature_mean = songs['time_signature'].mean()

#NA values are replaced with column averages
songs['instrumentalness'] = songs['instrumentalness'].fillna(instrumentalness_mean)
songs['acousticness'] = songs['acousticness'].fillna(acousticness_mean)
songs['time_signature'] = songs['time_signature'].fillna(time_signature_mean)

#Here we change the values in the dataset to be ratios instead of percentages
#This way the 2010-19 and the 2020 datasets all have the same units
songs['danceability'] = 0.01*songs['danceability']
songs['energy'] = 0.01*songs['energy']
songs['speechiness'] = 0.01*songs['speechiness']
songs['valence'] = 0.01*songs['valence']
songs['liveness'] = 0.01*songs['liveness']



###
########## 2020 songs
###
songs_20 = pd.read_csv(r'/Users/austineaton/Projects/spotify_project/songs_20.csv')

songs_20.rename(columns = {'Unnamed: 0':'Number'}, inplace=True)

#Drop certain columns
songs_20.drop(['Unnamed: 0.1', 'album'], axis=1, inplace=True)

#Here we change the values in the dataset to be ratios instead of percentages
#This way the 2010-19 and the 2020 datasets all have the same units
songs_20['length'] = 0.001*songs_20['length']

#Change the number of the 2020 songs
songs_20['Number'] = 603+songs_20['Number']



###
##########Merge the two separate dataframes
###
frames = [songs, songs_20]
all_songs = pd.concat(frames)

#reset the index
all_songs.reset_index(drop=True, inplace=True)