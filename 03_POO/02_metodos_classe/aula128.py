# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # Decorator
    def metodo_de_classe(cls): # cls (classe) indica que é método de classe
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome): # Como se fosse uma extensão da minha classe
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena') # Aqui eu chamo direto da classe e passo somente 1 parametro (factories)
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

Pessoa.metodo_de_classe()