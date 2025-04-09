"""
Retorno de valores das funções (return)
"""

def soma(x, y): # Por padrão, sem return, ela sempre retorna None
    if x > 10:
        return [10, 20]
    return x + y

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2) # Preciso que retorne algo pois estou retornando um valor a uma variavel
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))