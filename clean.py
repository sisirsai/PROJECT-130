import pandas as pd
df = pd.read_csv('overAll.csv')
del df['Luminosity']
df.drop_duplicates(inplace = True)
df.dropna(inplace = True)
df.to_csv('Cleaned_data.csv')