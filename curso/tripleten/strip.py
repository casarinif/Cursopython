import pandas as pd

df = pd.read_csv('music_log_raw.csv')

new_col_names = []

  # Itera sobre os nomes das colunas existentes
for name in df.columns:
    # Primeiro, remova os espaços no início e no final
    name_stripped = name.strip()
    # Em seguida, coloque todas as letras em minúsculas
    name_lowered = name_stripped.lower()
    # Por fim, substitua os espaços entre as palavras por sublinhados
    name_no_spaces = name_lowered.replace(' ', '_')
    # Adicione o novo nome à lista de novos nomes das colunas
    new_col_names.append(name_no_spaces)

# Atribui os novos nomes das colunas ao DataFrame
df.columns = new_col_names

print(df.columns)