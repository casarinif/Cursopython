import pandas as pd

cholera = pd.read_csv('cholera.csv')
print(cholera.isna().sum())

#A coluna 'imported_cases' agora tem todos os seus valores ausentes preenchidos com zeros.
#cholera['imported_cases'] = cholera['imported_cases'].fillna(0)

# percorrendo os nomes das colunas e substituindo valores ausentes com 0s
columns_to_replace = ['imported_cases']

for col in columns_to_replace:
    cholera[col].fillna(0, inplace=True)

print(cholera)

cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'])
print(cholera)

#removerá todas as colunas que tenham valores ausentes. Como 'notes'
#cholera = cholera.dropna(axis='columns')

#descartar apenas a coluna 'notes'
cholera = cholera.drop(labels=['notes'], axis='columns')
print(cholera)
