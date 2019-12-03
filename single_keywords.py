import pandas as pd
import itertools
import ast
import time
import json

def countKeywords(df):

    list_main = []

    for index, row in df.iterrows():
        try:
            list_keywords = ast.literal_eval(row['keywords'])
            # list_keywords = (row["keywords"])
           # list_keywords = [n.strip() for n in row["keywords"]]

            for keyword in list_keywords:
                row['single_keyword'] = keyword
                df = pd.DataFrame(row).transpose()
                list_main.append(df)
        except SyntaxError as er:
            print ("error", er)
            pass

    df = pd.concat(list_main)

    return df

df = pd.read_csv("data/Pantene/pantene_combined_keywords.csv", encoding='utf8')
df_main = countKeywords(df)

df_main.to_csv("data/Pantene/pantene_combined_keywords_single.csv")