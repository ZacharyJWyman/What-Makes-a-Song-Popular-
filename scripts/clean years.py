#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r'https://raw.githubusercontent.com/ZacharyJWyman/Spotify-API/master/data/all_songs.csv?token=APIXTTZ4TZDE2X7EMLMJ2627IGSQ2')


# In[4]:


data.drop(['Unnamed: 0', 'Number'], axis = 1, inplace=True)


# In[5]:


data.dtypes


# In[6]:


years = []
for i in data['release_date']:
    year = substring = i[:4]
    years.append(int(year))


# In[7]:


data['release_date'] = years


# In[10]:


data.to_csv(r'D:\Data Science\Spotify API\data\all_songs.csv')


# 
