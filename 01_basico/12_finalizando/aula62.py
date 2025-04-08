"""
Exercício Final

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = input("Digite um CPF (somente números): ")

# Verifica se tem 11 dígitos e todos são numéricos
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
else:
    # Cálculo do primeiro dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resultado = (soma * 10) % 11
    digito_1 = 0 if resultado > 9 else resultado

    # Cálculo do segundo dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (11 - i)
    soma += digito_1 * 2

    resultado = (soma * 10) % 11
    digito_2 = 0 if resultado > 9 else resultado

    # Verificação final
    if int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2:
        print("CPF válido!")
    else:
        print("CPF inválido!")
