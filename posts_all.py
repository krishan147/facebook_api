# token expires on january 24th
import pandas as pd
import time
import datetime
import requests

def facebook(handle, access_token):

    list_frames = []
    x = 1
    time.sleep(2)
    url = "https://graph.facebook.com/v4.0/" + handle + "?fields=posts.limit(100).until(1574679326).since(1543017600)%7Bmessage%2Ccreated_time%7D&access_token=" + access_token
    # likes, shares, comments https://graph.facebook.com/v4.0/216311481960_10154125934861961?fields=shares,likes.summary(true).limit(0),comments.summary(true).limit(0)&access_token=

    data = requests.get(url).json()

    if 'posts' in str(data):
        df = pd.DataFrame(data['posts']['data'])
        handle = handle.replace('\n','')
        df['handle'] = handle
        list_frames.append(df)
        last_created_date = df['created_time'].min()
        data_posts = data["posts"]

        while 'next' in data_posts["paging"] and last_created_date > '2018-09-21T00:00:00+0000':

            url_paging = data_posts["paging"]["next"]
            data_paging = requests.get(url_paging).json()
            df_paging = pd.DataFrame(data_paging['data'])
            list_frames.append(df_paging)
            data_posts = data_paging
            x = x + 1
            time.sleep(7)

        if 'next' not in data["posts"]["paging"] or last_created_date > '2018-09-21T00:00:00+0000':

            df = pd.concat(list_frames)

            return df

credentials_file = open("credentials.txt", "r")
access_token = credentials_file.read()

with open("handles.txt", "r") as handles:
    for handle in handles:
        handle.strip()
        print (handle)
        df = facebook(handle, access_token)
        df.to_csv("data/"+handle+".csv")