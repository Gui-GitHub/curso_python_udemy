# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...') #Usei o nome da instancia com self.nome


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome) #fusca.nome é literalmente self.nome
fusca.acelerar() #Não precisa de print

celta = Carro(nome='Celta') # Podemos passar argumentos nomeados também, já que é um método
print(celta.nome)
celta.acelerar()