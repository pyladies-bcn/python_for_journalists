# -*- coding: utf-8 -*-
"""
Created on 
@author: PyLadiesBCN (@PyLadiesBCN)
"""

"""
Go to apps.twitter.com
Log in
Create a new app
Get consumer key and consumer secret
Get access token and access token secret

Search will be rate limited at 180 queries per 15 minute window for the time 
being, but we may adjust that over time. 
"""

"""
We import the library tweepy
("pip install tweepy" if it's not installed)
"""
import tweepy
import json
import pandas as pd
import csv

"""
We use our authorization keys
"""
auth = tweepy.OAuthHandler("INTRODUCIR CONSUMER KEY", "INTRODUCIR CONSUMER SECRET")
auth.set_access_token("INTRODUCIR ACCESS TOKEN", "INTRODUCIR ACCESS TOKEN SECRET")

api = tweepy.API(auth)

"""
Read our timeline and save results in a dataframe
"""
timeline = api.home_timeline(count = 100)
usuarios = []
screen_name = []
texto = []
retweet_count = []
for i in range(len(timeline)):
    usuarios.append(timeline[i].user.name)
    screen_name.append(timeline[i].user.screen_name)
    texto.append(timeline[i].text)
    retweet_count.append(timeline[i].retweet_count)

df = pd.DataFrame(usuarios)
df["user"] = usuarios
df["screen_name"] = screen_name
df["rt"] = retweet_count
df["text"] = texto  
del df[0]  

df1 = df.sort(["rt"], ascending=False)

file = open("mi_timeline.csv", "w")
df1.to_csv(file, sep=",", encoding = "utf-8")

"""
Search on twitter and save results in a dataframe
"""

busqueda_usuario=[]
busqueda_texto=[]
busqueda_created_at = []
for tweet in tweepy.Cursor(api.search,
                           q="Obama",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang= "en",
                           since='2015-01-01',
                           until='2015-03-20').items(100):
    busqueda_created_at.append(tweet.created_at)
    busqueda_usuario.append(tweet.user.name)    
    busqueda_texto.append(tweet.text)
    

df2 = pd.DataFrame(busqueda_created_at)
df2["fecha"] = busqueda_created_at
df2["usuario"] = busqueda_usuario
df2["texto"] = busqueda_texto
del df2[0]

file = open("mi_busqueda.csv", "w")
df2.to_csv(file, sep=",", encoding = "utf-8")
