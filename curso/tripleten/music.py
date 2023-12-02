import pandas as pd

df = pd.read_csv('music_log_raw.csv')

columns_to_replace = ['genre', 'Artist', 'track']

# Substituir valores ausentes nas colunas especificadas por 'no_info'
for col in columns_to_replace:
    df[col].fillna('no_info', inplace=True)

# Substituir valores ausentes na coluna 'total play' por 0
df['total play'].fillna(0, inplace=True)

# Verificar novamente o número de valores ausentes
print(df.isna().sum())
print(df.duplicated())
