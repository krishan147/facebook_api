# token expires on january 24th
import pandas as pd
import time
import datetime
import requests
import json

def facebook(handle, access_token):

    time.sleep(4)
    url = "https://graph.facebook.com/v4.0/" + handle + "?fields=posts.limit(100).until(1574679326).since(1543017600)%7Bmessage%2Ccreated_time%7D&access_token=" + access_token
    # likes, shares, comments https://graph.facebook.com/v4.0/216311481960_10154125934861961?fields=shares,likes.summary(true).limit(0),comments.summary(true).limit(0)&access_token=

    data = requests.get(url).json()
    posts = data['posts']['data']
    list_post = []
    list_created_time = []
    list_post_id = []

    for post_data in posts:
        if 'message' not in post_data:
            list_post.append("")
        else:
            post = post_data['message']
            post = post.replace("\n", " ")
            list_post.append(post)

        created_time = post_data['created_time']
        post_id = post_data['id']
        list_created_time.append(created_time)
        list_post_id.append(post_id)

    if 'posts' in str(data):
        df = pd.DataFrame(data['posts']['data'])
        last_created_date = df['created_time'].min()
        data_posts = data["posts"]

        while 'next' in data_posts["paging"] and last_created_date > '2017-09-21T00:00:00+0000':

            url_paging = data_posts["paging"]["next"]
            data_paging = requests.get(url_paging).json()

            for post_data_paging in data_paging['data']:

                if 'message' not in post_data_paging:
                    list_post.append("")
                else:
                    post = post_data_paging['message']
                    post = post.replace("\n", " ")
                    list_post.append(post)

                created_time = post_data_paging['created_time']
                post_id = post_data_paging['id']
                list_created_time.append(created_time)
                list_post_id.append(post_id)
            data_posts = data_paging
            time.sleep(7)

        if 'next' not in data["posts"]["paging"] or last_created_date > '2017-09-21T00:00:00+0000':

            df = pd.DataFrame(data = {
                'post_id':list_post_id,
                'created_time':list_created_time,
                'post':list_post,
            })

            df['handle'] = handle

            return df

credentials_file = open("credentials.txt", "r")
access_token = credentials_file.read()

with open("handles.txt", "r") as handles:
    for handle in handles:
        handle = handle.replace('\n', '')
        print (handle)
        df_main = facebook(handle, access_token)

        df_main.to_csv("data/"+handle+".csv")