import pandas as pd

df = pd.read_excel('rozloha_fin.xlsx')

#print(df)

# Assuming your DataFrame is named 'df'
summed_areas = df.groupby('pou')['vymera'].sum()

summed_areas_df = summed_areas.reset_index()

print(summed_areas_df)

summed_areas_df.to_excel('summed_areas.xlsx')