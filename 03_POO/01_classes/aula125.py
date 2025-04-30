# Atributos de classe
class Pessoa:
    ano_atual = 2022 # Isso é um atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade # Acessando o atributo da classe


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1 # Modificando o atributo

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())