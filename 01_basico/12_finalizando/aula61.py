
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = 0
num = 10
soma = 0
multiplicador = 0

cpf = input("Digite um CPF (somente números): ")

# Verifica se tem 11 dígitos
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
else:
    multiplicador = 10

    # Percorre os 9 primeiros dígitos do CPF
    for i in range(9):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1

    resultado = (soma * 10) % 11
    digito_1 = 0 if resultado > 9 else resultado

    print(f"O primeiro dígito verificador calculado é: {digito_1}")
