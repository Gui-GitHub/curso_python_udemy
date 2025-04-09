"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args): # Basciamente não preciso dizer todos os argumentos NÃO nomeados, empacotando tudo
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma(1, 2, 3, 4747, 29, 8)
# print(soma_1)

soma_2 = soma(4, 5, 6)
# print(soma_2)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# print(numeros)
# print(*numeros)
outra_soma = soma(*numeros) # Coloco * para desempacotar os valores
print(outra_soma)

print(sum(numeros)) # sum faz literalmente a soma dos valores, como na def