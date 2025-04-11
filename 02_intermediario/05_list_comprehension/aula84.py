# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10))) Vamos fazer a mesma lista abaixo
lista = []
for numero in range(10):
    lista.append(numero)

listaC = [ # List comprehesion:
    numero * 2
    for numero in range(10)
]
print(listaC)

##################################################################

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # if ternário
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')

########################################################################

# Introdução à List comprehension em Python
# Filtro

import pprint # Print bonito

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# p(novos_produtos)
# lista = [n for n in range(10) if n < 5] # Lista com o filtro, usando o if
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # Filtro
]
p(novos_produtos)