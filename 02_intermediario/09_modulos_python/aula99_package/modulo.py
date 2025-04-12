# __all__ = [ personaliza o * quando é chamado
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]

# from modulo_b import fala_oi # Funciona aqui pois são irmãos
# from aula99_package.modulo_b import fala_oi
# from .modulo_b import fala_oi # Se eu somente digitar .modulo_b, é reconhecido o nome do package

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'
# falar_oi()