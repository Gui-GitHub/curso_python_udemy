# Aqui é utilizado o método Format
# Tudo em python é objeto e um objeto possui métodos como o 'format'
# Parametro nomeado -> Nome do Parametro(nome1) Argumento(a)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)