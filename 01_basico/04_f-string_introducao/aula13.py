# Veja que com o f-string, as váriaveis ficam com chaves {}, mas ficam mais simples de ler também
# Formatar casas decimais (:.2f) para termos 2 casas decimais

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# "f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu imc é
# 29.32