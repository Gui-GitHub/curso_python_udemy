# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor_tinta()
# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor # Independente do nome da váriavel, ele consegue pegar o nome da cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property # Faz um método se comportar como atributo, não preciso de ()
    def cor(self):
        print('PROPERTY:')
        return self.cor_tinta # Utilizei aqui como um getter

    @property
    def cor_tampa(self):
        return 123456

###########################


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa) # Chamo eles sem ()

####################################

