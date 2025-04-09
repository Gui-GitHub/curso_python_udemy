"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(1, z=2, y=5) # Eu saio da ordem, nomeando o parametro e dando valor a eles | Geralmente ou nomeie todos ou não nomeie todos.

print(1, 2, 3, sep='-')