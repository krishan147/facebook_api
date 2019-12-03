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

    time.sleep(3)

    print (likes,",",shares,",",comments)

    return likes, shares, comments

#encoding='windows-1252'
credentials_file = open("credentials.txt", "r")
access_token = credentials_file.read()
df = pd.read_csv('data/Pantene/pantene_combined_keywords.csv', encoding="utf8")
list_post_id = df['post_id'].tolist()


# filter1 = df["Filled"] != "Y"
# filter2 = df["handle"] != "AldiUK"
# df.where(filter1, inplace = True)
# df.where(filter2, inplace = True)
# df = df[(df["Filled"] != "Y") | (df["handle"] != "AldiUK") | (df["Filled"] != "Y") & (df["handle"] != "AldiUK")]

# df = df.loc[df['Filled'] != "Y"]
# df = df.loc[df['handle'] != "AldiUK"]

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

df.to_csv("data/Pantene/pantene_combined_keywords_stats.csv")