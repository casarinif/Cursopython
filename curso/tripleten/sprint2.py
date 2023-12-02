import pandas as pd

import pandas as pd

# as distâncias são armazenadas em uma lista de listas
measurements = [['Sun', 146, 152],
                                ['Moon', 0.36, 0.41],
                                ['Mercury', 82, 217],
                                ['Venus', 38, 261],
                                ['Mars', 56, 401],
                                ['Jupiter', 588, 968],
                                ['Saturn', 1195, 1660],
                                ['Uranus', 2750, 3150],
                                ['Neptune', 4300, 4700],
                                ['Halley\'s comet', 6, 5400]]

# os nomes das colunas são armazenados na variável de cabeçalho
header = ['Celestial bodies ','MIN', 'MAX']

# armazenando o DataFrame na variável celestial
celestial = pd.DataFrame(data=measurements, columns=header)
columns_new ={
    "Celestial bodies ": "celestial_bodies",
    "MIN": "min_distance",
    "MAX": "max_distance",
    }

celestial = celestial.rename(columns = columns_new)
print(celestial.columns)