# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário. (como na lista)
# Usamos as chaves - {} - ou a classe dict() para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'], end='\n\n')

for chave in pessoa:
    print(chave, pessoa[chave])

#############################################################

# Manipulando chaves e valores em dicionários
pessoa = {}
chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome'] # Possível apagar chaves (CRUD)
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None: #Get tenta obter uma chave, retorna none caso não exista
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

############################################################

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0) # Caso não existisse idade, seria 0 o retorno do print
print(pessoa['idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

############################################################

# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy) não entra dentro de subniveis de um dicionario

import copy # Aqui eu poderia usar um Deep Copy com copy.deepcopy()

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

############################################################

# Métodos úteis dos dicionários em Python
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome']) Aqui da erro
# print(p1.get('nome', 'Não existe')) Aqui retorna None

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30, Posso criar novas chaves também
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)