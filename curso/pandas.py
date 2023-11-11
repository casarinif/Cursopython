import pandas as pd

from IPython.utils import data

# Inicializa o módulo Pandas e define várias opções de configuração.
pandas.set_option('display.max_rows', None)


# Cria um DataFrame da lista.
df = pd.DataFrame(data)

# Exibe o DataFrame.
print(df)

