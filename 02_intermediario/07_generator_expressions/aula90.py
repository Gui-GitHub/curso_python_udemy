import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__ | thunder -> '__'
print(next(iterator))

lista = [n for n in range(1000000)] # Esta sendo salvo todos na memória, podendo acessar indice por indice e tamanho completo com len()
generator = (n for n in range(1000000)) # Entrega um valor por vez, trazendo um por um com next()

print(sys.getsizeof(lista)) # Para saber o tamanho da lista em Bytes
print(sys.getsizeof(generator)) # Aqui temos somente 104 bytes em comparação a lista

# for n in generator:
#     print(n)