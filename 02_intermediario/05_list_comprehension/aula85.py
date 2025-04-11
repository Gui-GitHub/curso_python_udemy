lista1 = []
for x in range(3):
    for y in range(3):
        lista1.append((x, y))
lista2 = [ # Mesmo código acima basicamente
    (x, y) # Aqui vem o mapeamento
    for x in range(3)
    for y in range(3)
]
lista3 = [
    [(x, letra) for letra in 'Luiz'] # Uma list comprehesion dentro de outra
    for x in range(3)
]

print(lista1)
print(lista2)
print(lista3)