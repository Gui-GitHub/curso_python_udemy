# Exercícios

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número: ')

try:
    numero_convertido = int(numero)
    if numero_convertido % 2 == 0:
        print(f'O número {numero_convertido} é par!')
    else:
        print(f'O número {numero_convertido} é impar')
except:
    print('Digite um número inteiro por favor!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Que horas são agora? ')

try:
    horario_int = int(horario)
    if horario_int <= 11:
        print('Bom dia!')
    elif horario_int <= 18:
        print('Boa tarde')
    elif horario_int <= 24:
        print('Boa noite')
    else:
        print(f'Não reconheço a hora {horario_int}')
except:
    print('Digite um número inteiro por favor!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Escreva seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('Seu nome é curto')
    elif tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite mais de uma letra.')