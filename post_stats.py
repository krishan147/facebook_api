# token expires on january 24th
import pandas as pd
import time
import datetime
import requests
import json

def facebookStats(access_token, post_id):

    time.sleep(2)
    url = "https://graph.facebook.com/v4.0/"+post_id+"?fields=shares,likes.summary(true).limit(0),comments.summary(true).limit(0)&access_token=" + access_token
    data = requests.get(url).json()
    try:
        shares = data['shares']['count']
    except KeyError:
        shares = 0

    try:
        likes = data['likes']['summary']['total_count']
    except KeyError:
        likes = 0
    try:
        comments = data['comments']['summary']['total_count']
    except KeyError:
        comments = 0

    time.sleep(6)

    print (likes,",",shares,",",comments)

    return likes, shares, comments

credentials_file = open("credentials.txt", "r")
access_token = credentials_file.read()
df = pd.read_csv('data/haircare_combined.csv',encoding='utf8')
list_post_id = df['post_id'].tolist()

list_likes = []
list_shares = []
list_comments = []

for post_id in list_post_id:
    likes, shares, comments = facebookStats(access_token, post_id)
    list_likes.append(likes)
    list_shares.append(shares)
    list_comments.append(comments)

df['likes'] = list_likes
df['shares'] = list_shares
df['comments'] = list_comments

df.to_csv("data/haircare_combined_stats.csv")