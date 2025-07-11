# secrets gera números aleatórios seguros
import secrets

# import string as s
# from secrets import SystemRandom as Sr

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))  # noqa: E501
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"  # noqa: E501

random = secrets.SystemRandom()

print(secrets.randbelow(100))
print(secrets.choice([10, 11, 12]))

# Funções:
# seed
#   -> NÃO FAZ NADA
random.seed(10)

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