import pandas as pd

# Ler um arquivo CSV
df = pd.read_csv('music_log_raw.csv')

# Imprimir as primeiras 5 linhas do DataFrame
print(df.head())

# Ler um arquivo Excel
df2 = pd.read_excel('music_log_raw.xlsx')

# Imprimir as últimas 5 linhas do DataFrame
print(df2.tail())

# Encontrar a média usando a notação completa e a expressão ==
mean_duration = df.loc[df['genre'] == 'pop', 'total play'].mean()

# Encontrar o número de músicas usando a notação abreviada e a expressão <=
count_duration = df[df['total play'] <= 130]['total play'].count()

# Encontrar a média usando a notação abreviada e a expressão ==
sum_duration = df[df['genre'] == 'pop']['total play'].sum()

# Ler novamente o arquivo CSV (talvez isso não seja necessário, dependendo do que você deseja alcançar)
df3 = pd.read_csv('music_log_raw.csv')

# Imprimir as primeiras 5 linhas do DataFrame
print(df3.head())
