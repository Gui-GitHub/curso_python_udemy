"""
Interpolação básica de strings basicamente o format
Sempre com o % com o tipo
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
Colocar entre parenteses a ordem
Como se fosse placeholders que são declarados depois da %

"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))