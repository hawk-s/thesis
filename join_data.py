import pandas as pd

df = pd.read_excel('lexikon_2018.xlsx')
df_main = pd.read_excel('obce_na_join.xlsx')
#print(df_main)
#print(df_districts)
#print(df['orp_obec'])
#print(df_main['orp_obec'])

joined = df_main.merge(df, on = 'orp_obec', how = 'left')

print(joined)
joined.to_excel('pou_joined_w_roz_final.xlsx')
