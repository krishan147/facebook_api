import pandas as pd
import itertools
import ast
import time

def countKeywords(df):

    list_main = []

    for index, row in df.iterrows():
        list_keywords = ast.literal_eval(row['keywords'])
        for keyword in list_keywords:
            row['single_keyword'] = keyword
            df = pd.DataFrame(row).transpose()
            list_main.append(df)

    df = pd.concat(list_main)

    return df

df = pd.read_csv("data/haircare_combined_keywords.csv", encoding='utf8')
df_main = countKeywords(df)

df_main.to_csv("data/haircare_combined_keywords_skeywords.csv")