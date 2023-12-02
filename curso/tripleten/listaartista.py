import pandas as pd

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit']
]

columns = ['Artista', 'Nome das Musicas']

tabela = pd.DataFrame(data=music, columns=columns)

print(tabela)

