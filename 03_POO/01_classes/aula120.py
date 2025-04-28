# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de Classes.

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str)) #str é uma classe padrão do python

# class Pessoa:
#     ...


# p1 = Pessoa()
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

# p2 = Pessoa()
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

# print(p1.nome)
# print(p1.sobrenome)

# print(p2.nome)
# print(p2.sobrenome)

# Introdução ao método __init__ (inicializador de atributos)
# 'self' sempre será nosso primeiro parametro
# self é o objeto da minha classe. Assim podemos receber argumentos agora
# self.nome, digo que 'Luiz' será o atributo nome

class Pessoa:
    def __init__(self, nome, sobrenome): #Inicializa os meus atributos da classe
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)