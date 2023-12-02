import pandas as pd

df = pd.read_csv('music_log_raw.csv')

# Subconjunto para o gênero 'pop'
pop = df[df['genre'] == 'pop']

# Subconjunto para o gênero 'ambient' e remoção de duplicatas
ambient = df[df['genre'] == 'ambient'].drop_duplicates()

# Contagem de duplicatas no subconjunto 'pop'
duplicates_pop = pop.duplicated().sum()

# Contagem de duplicatas no subconjunto 'ambient' após a remoção de duplicatas
duplicates_ambient = ambient.duplicated().sum()

print('Número de duplicatas no subconjunto "pop":', duplicates_pop)
print('Número de duplicatas no subconjunto "ambient" após remover duplicatas:', duplicates_ambient)

