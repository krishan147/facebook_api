import pandas as pd

df = pd.read_csv('data/haircare_combined.csv')

df = df[df['post'].str.contains("pantene|aussie|herbal|shoulders|shampoo|conditioner|tressemme")==True]

#df = df.a.str.contains(pattern)

df.to_csv("data/haircare_combined_haironly.csv")