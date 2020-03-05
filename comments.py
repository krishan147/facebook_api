import pandas as pd
import time
import datetime
import requests
import json
from time import mktime

end_date = 1583419446  # 1574679326
start_date = end_date - 31536000

def facebook(handle, access_token):

    time.sleep(4)

    end_date = 1583419446 #1574679326
    start_date = end_date - 31536000

    handle = "walkers"

    url = "https://graph.facebook.com/v4.0/" + handle + "?fields=posts.limit(100).until("+str(end_date)+").since("+str(start_date)+")%7Bmessage%2Ccreated_time%2Ccomments%7D&access_token=" + access_token
    data = requests.get(url).json()

    if "posts" in str(data):
        posts = data['posts']['data']

        #print (posts)


        for comments in data['posts']['data']:
            print (comments)
            
            # krishan you can hit next in order to get the next page of comments

    #     list_post = []
    #     list_created_time = []
    #     list_post_id = []
    #
    #     for post_data in posts:
    #         if 'message' not in post_data:
    #             list_post.append("")
    #         else:
    #             post = post_data['message']
    #             post = post.replace("\n", " ")
    #             list_post.append(post)
    #
    #         created_time = post_data['created_time']
    #         post_id = post_data['id']
    #         list_created_time.append(created_time)
    #         list_post_id.append(post_id)
    #
    #     if 'posts' in str(data):
    #         df = pd.DataFrame(data['posts']['data'])
    #         last_created_date = df['created_time'].min()
    #         data_posts = data["posts"]
    #         last_created_date = datetime.datetime.strptime(last_created_date, '%Y-%m-%dT%H:%M:%S+0000')
    #         last_created_date = mktime(last_created_date.timetuple())
    #
    #         while 'next' in data_posts["paging"] and last_created_date < end_date:
    #
    #             url_paging = data_posts["paging"]["next"]
    #             data_paging = requests.get(url_paging).json()
    #
    #             for post_data_paging in data_paging['data']:
    #
    #                 if 'message' not in post_data_paging:
    #                     list_post.append("")
    #                 else:
    #                     post = post_data_paging['message']
    #                     post = post.replace("\n", " ")
    #                     list_post.append(post)
    #
    #                 created_time = post_data_paging['created_time']
    #                 post_id = post_data_paging['id']
    #                 list_created_time.append(created_time)
    #                 list_post_id.append(post_id)
    #             data_posts = data_paging
    #             time.sleep(7)
    #
    #         if 'next' not in data["posts"]["paging"] or last_created_date < end_date:
    #
    #             df = pd.DataFrame(data = {
    #                 'post_id':list_post_id,
    #                 'created_time':list_created_time,
    #                 'post':list_post,
    #             })
    #
    #             df['handle'] = handle
    #
    #             return df
    # else:
    #     print ("not made any posts in last year")
    #     df = pd.DataFrame(data={
    #         'post_id': [],
    #         'created_time': [],
    #         'post': [],
    #     })
    #     return df

credentials_file = open("credentials.txt", "r")
access_token = credentials_file.read()

with open("handles.txt", "r") as handles:
    for handle in handles:
        handle = handle.replace('\n', '')

        df_main = facebook(handle, access_token)
        df_main.to_csv("data/"+handle+".csv")
        time.sleep(10)