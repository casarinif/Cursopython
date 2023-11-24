import csv
import os

# Obtém o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Constrói os caminhos completos para os arquivos
caminho_arquivo_2018 = os.path.join(diretorio_atual, '2018m.csv')
caminho_arquivo_2019 = os.path.join(diretorio_atual, '2019w.csv')

# Abre os arquivos CSV em modo de leitura
with open(caminho_arquivo_2018, newline='') as csvfile_2018:
    leitor_csv_2018 = csv.reader(csvfile_2018)
    dados_2018 = [linha for linha in leitor_csv_2018]

with open(caminho_arquivo_2019, newline='') as csvfile_2019:
    leitor_csv_2019 = csv.reader(csvfile_2019)
    dados_2019 = [linha for linha in leitor_csv_2019]

# Exibe os dados lidos dos arquivos CSV
print("Dados de 2018:", dados_2018)
print("Dados de 2019:", dados_2019)
