import pandas as pd

df = pd.read_csv('music_log_raw.csv')

print(df.head(10))
print(df.isna().sum())