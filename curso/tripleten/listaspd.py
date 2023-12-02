import pandas as pd

state_animals = [
    ['Alabama', 'black bear'],
    ['Alaska', 'moose'],
    ['Arizona', 'ringtail'],
    ['Arkansas', 'white-tailed deer'],
    ['California', 'grizzly bear'],
    ['Colorado', 'rocky Mt. bighorn sheep'],
    ['Connecticut', 'sperm whale'],
    ['Delaware', 'gray fox'],
    ['Florida', 'manatee'],
    ['Georgia', 'white-tailed deer']
]

# Escreva seu código aqui
col_names = ['state','animal']

df = pd.DataFrame(state_animals,columns=col_names)

print(df)