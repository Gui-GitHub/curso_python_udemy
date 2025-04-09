# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(multiplicar(2,4,5))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    if x%2 == 0:
        return 'Par'
    return 'Ímpar'

print(par_impar(36))