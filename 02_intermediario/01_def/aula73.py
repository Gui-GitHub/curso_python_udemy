"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz') # Estou chamando os argumentos separados por ',' graças a função executa() que possui um '*args'
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)