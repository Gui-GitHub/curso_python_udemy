"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome): # Passando o segundo parametro para a outra def, para se tornar mais dinamico
        return f'{saudacao}, {nome}!'
    return saudar


bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(bom_dia(nome))
    print(boa_noite(nome))