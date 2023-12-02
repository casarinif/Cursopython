import pandas as pd

rating = ['date', 'name', 'points']
players = [
        ['2018.01.01',  'Rafael Nadal', 10645],
                ['2018.01.08',  'Rafael Nadal', 10600],
                ['2018.01.29',  'Rafael Nadal', 9760],
                ['2018.02.19',  'Roger Federer', 10105],
                ['2018.03.05',  'Roger Federer', 10060],
                ['2018.03.19',  'Roger Federerr', 9660],
                ['2018.04.02',  'Rafael Nadal Parera', 8770],
                ['2018.06.18',  'Roger Fedrer', 8920],
                ['2018.06.25',  'Rafael Nadal Parera', 8770],
                ['2018.07.16',  'Rafael Nadal Parera', 9310],
                ['2018.08.13',  'Rafael Nadal Parera', 10220],
                ['2018.08.20',  'Rafael Nadal Parera', 10040],
                ['2018.09.10',  'Rafael Nadal Parera', 8760],
                ['2018.10.08',  'Rafael Nadal Parera', 8260],
                ['2018.10.15',  'Rafael Nadal Parera', 7660],
                ['2018.11.05',  'Novak Djokovic', 8045],
                ['2018.11.19',  'Novak Djokovic', 9045]
]
tennis = pd.DataFrame(data=players, columns=rating)

tennis['name'] = tennis['name'].replace('Roger Federerr', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Roger Fedrer', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera')

print(tennis)
print(tennis['name'].unique())
print(tennis['name'].nunique())