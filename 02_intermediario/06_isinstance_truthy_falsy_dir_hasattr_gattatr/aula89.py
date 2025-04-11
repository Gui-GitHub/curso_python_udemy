
# dir, hasattr e getattr em Python
# dir(string) me trás todos os atributos que aquele elemento possui, pelo terminal do debugger
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo): # Ou (string, upper)
    print('Existe upper')
    print(getattr(string, metodo)()) # Ou print(string.strip()), ele pega o texto da váriavel e tenta chamar ele
else:
    print('Não existe o método', metodo)
