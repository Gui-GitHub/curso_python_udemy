# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import json # Módulo Json

caminho_arquivo = 'C:\\Users\\guilh\\OneDrive\\Documentos\\curso_python_udemy\\02_intermediario\\13_context_manager\\aula117.json'

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: # Criando o arquivo, .json
    json.dump( # Gerar arquivo
        pessoa,
        arquivo,
        ensure_ascii=False, # Agora ele coloca acentuação
        indent=2, # Deixa o 'dado' formatado ao invés de uma única linha
    )

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) # load serve para carregar um arquivo (nesse caso o json)
    # print(pessoa) # Joga o dicionário
    # print(type(pessoa)) # Me diz o tipo
    print(pessoa['nome']) # Traz um valor especifico dado o seu valor