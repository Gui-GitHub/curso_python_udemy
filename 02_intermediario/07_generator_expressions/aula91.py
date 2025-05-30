
# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # Ele pausa a execução
        n += 1

        if n > maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)
