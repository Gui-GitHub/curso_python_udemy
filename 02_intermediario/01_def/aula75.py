# Exercícios

# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(multiplicador):
    def multiplicar (num):
        return num*(multiplicador)
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

for num in [2, 4]:
    print(duplicar(num))
    print(triplicar(num))
    print(quadruplicar(num))