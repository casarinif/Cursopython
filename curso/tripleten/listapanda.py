import pandas as pd

# Preparando os dados e os nomes das colunas
atlas = [
    ['France', 'Paris'],
    ['Russia', 'Moscow'],
    ['China', 'Beijing'],
    ['Mexico', 'Mexico City'],
    ['Egypt', 'Cairo'],
]
geography = ['country', 'capital']

# Fazendo um DataFrame
world_map = pd.DataFrame(data=atlas, columns=geography)

# Imprimindo o DataFrame
print(world_map)

