
# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

import sys

platform = 'A minha é'
print(sys.platform) #win32
print(platform)
print(platform, sys.platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

from sys import exit, platform

print(platform) # Chamo direto, mas tenho que tomar cuidado, pois se eu tiver uma váriavel la em cima ela subscreve

# alias 1 - import nome_modulo as apelido

import sys as s # Dei um apelido ao sys

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido

from sys import exit as ex
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import * # É um pouco obscuro, não estou vendo o que estou importanto

print(platform)
exit()