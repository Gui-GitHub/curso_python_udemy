"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] inicio : fim : passo (final pega 1 a mais, pois ele mesmo não é incluido)
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])

print(variavel[:5])

print(variavel[-8:-2])

print(variavel[::-1])

print(len(variavel))