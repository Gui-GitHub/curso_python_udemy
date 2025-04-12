# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula99_package
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *
# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')

# print(soma_do_modulo(1, 2)) # from aula99_package.modulo import * ou from aula99_package.modulo import soma_do_modulo (melhor)
# print(modulo.soma_do_modulo(1, 2)) # from aula99_package import modulo
# print(aula99_package.modulo.soma_do_modulo(1, 2)) # import aula99_package.modulo
# print(variavel) # from aula99_package.modulo import soma_do_modulo
# print(nova_variavel) # from aula99_package.modulo import soma_do_modulo

#from aula99_package.modulo import fala_oi # Importação relativa ao package e módulos

# fala_oi()

from aula99_package import falar_oi, soma_do_modulo # Agora usando __init__ consigo importar tudo

print(soma_do_modulo(2, 3))
falar_oi() #  F2 altera em todos os lugares o nome da def