# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): # Tenho acesso a este parametro em qualquer lugar do escopo
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # Iner function, alinhada, uma função dentro da outra
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) # Ele executa a minha função decoradora caso não tenha () mesmo sem parametro
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)