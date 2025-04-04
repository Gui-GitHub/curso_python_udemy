# Exercício

"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)

indice = 0
novo_nome = ''

while indice < tamanho_nome:
    letra = nome[indice] 
    novo_nome += f'*{letra}'
    indice += 1

print(f'O nome gerado é {novo_nome}')