import json

from aula127_a import CAMINHO, Pessoa

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p1 = Pessoa(**pessoas[1])
    