import pandas as pd

df = pd.read_csv('music_log_raw.csv')

pop = df[df['genre'] == 'pop'].copy()

# Escreva seu código aqui
pop.drop_duplicates(inplace=True)
num = pop.duplicated().sum()

print(num)