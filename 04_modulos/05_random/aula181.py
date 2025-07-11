# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(f'Número aleatório entre 10 e 20 com passo 2: {r_range}')

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(f'Número aleatório entre 10 e 20 sem passo: {r_int}')

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(f'Número flutuante aleatório entre 10 e 20 sem passo: {r_uniform}')
print()

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
novos_nomes1 = random.shuffle(nomes)
print(f'Embaralhando lista ORIGINAL: {nomes}, (Retorna none): {novos_nomes1}')
print()

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes2 = random.sample(nomes, k=3)
print(f'Lista original: {nomes}')
print(f'Escolhe elementos da lista e retorna outro iterável (k): {novos_nomes2}')
print()

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes3 = random.choices(nomes, k=3)
print(f'Lista original: {nomes}')
print(f'Escolhe elementos da lista e retorna outro iterável (k) e pode repetir valores: {novos_nomes3}')
print()

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))