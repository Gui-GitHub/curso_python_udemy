# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)  # Formato de dicionário

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereco'])

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)